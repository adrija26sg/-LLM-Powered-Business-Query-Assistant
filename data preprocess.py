import pandas as pd
import mysql.connector
from datetime import datetime

# Load the CSV file
file_path = r'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\ncbi virus.csv'
df = pd.read_csv(file_path)

# Clean and format dates
def parse_date(date_str):
    try:
       
        return datetime.strptime(date_str, '%d-%m-%Y').date()
    except ValueError:
   
        if len(date_str) == 4:
            return datetime.strptime(date_str, '%Y').date()
        return None

df['VRL'] = df['VRL'].apply(lambda x: parse_date(x) if pd.notnull(x) else None)
df['COLLECTION DATE'] = df['COLLECTION DATE'].apply(lambda x: parse_date(x) if pd.notnull(x) else None)

#  MySQL
cnx = mysql.connector.connect(user=' ', password=' ',
                              host='127.0.0.1', database='ncbi_database')
cursor = cnx.cursor()

# Insert data into the MySQL table
for _, row in df.iterrows():
    insert_query = """
    INSERT INTO virus_data 
    (serial_no, accession_no, organism_name, vrl_date, species, genome_length, geo_location, host_species, collection_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data_tuple = (
        row['S.No.'], row['ACCESSION NO.'], row['ORGANISM NAME'], row['VRL'],
        row['SPECIES'], row['LENGTH'], row['GEO LOCATION'], row['HOST'], row['COLLECTION DATE']
    )
    cursor.execute(insert_query, data_tuple)

cnx.commit()
cursor.close()
cnx.close()
