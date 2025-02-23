from langchain_core.prompts import ChatPromptTemplate

sql_generation_prompt = ChatPromptTemplate.from_template("""
Below is the schema of a MySQL database. Based on it, convert the user question into an accurate SQL query.

{schema}

question: {question}
SQL query:
(Return only the SQL query without explanation)
""")

sql_response_prompt = ChatPromptTemplate.from_template("""
Given the database schema and SQL result below, generate a human-friendly answer to the user's question.

{schema}

question: {question}
SQL query: {query}
Result: {result}
Response:
""")
