<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCBI Virus Database Search</title>
</head>
<body>
    <h1>Search Virus Data</h1>
    <form method="GET" action="">
        <input type="text" name="query" placeholder="Enter organism name, species, etc." required>
        <button type="submit">Search</button>
    </form>

    <?php
    if (isset($_GET['query'])) {
        $query = $_GET['query'];

        // Database connection
        $conn = new mysqli('127.0.0.1', 'your_username', 'your_password', 'ncbi_database');
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // SQL query
        $sql = "SELECT * FROM virus_data WHERE organism_name LIKE '%$query%' OR species LIKE '%$query%' OR geo_location LIKE '%$query%'";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
            echo "<table border='1'><tr><th>S.No</th><th>Accession No.</th><th>Organism Name</th><th>VRL Date</th><th>Species</th><th>Genome Length</th><th>Geo Location</th><th>Host Species</th><th>Collection Date</th></tr>";
            while($row = $result->fetch_assoc()) {
                echo "<tr><td>{$row['serial_no']}</td><td>{$row['accession_no']}</td><td>{$row['organism_name']}</td><td>{$row['vrl_date']}</td><td>{$row['species']}</td><td>{$row['genome_length']}</td><td>{$row['geo_location']}</td><td>{$row['host_species']}</td><td>{$row['collection_date']}</td></tr>";
            }
            echo "</table>";
        } else {
            echo "No results found.";
        }
        $conn->close();
    }
    ?>

</body>
</html>
