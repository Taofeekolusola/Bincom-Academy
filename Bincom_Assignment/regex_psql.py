import re
import psycopg2

# Your PostgreSQL database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'taofeek',
    'password': 'adeshina123',
    'host': 'localhost',
    'port': '5432'
}

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(**db_params)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# HTML text
html_text = '<tr align="right"><td>12</td><td>Andrew</td><td>Addison</td></tr>'

# Define the regular expression pattern
pattern = re.compile(r'<tr align="right"><td>(\d+)</td><td>(.*?)</td><td>(\w+)</td></tr>')

# Use the pattern to find matches in the HTML text
match = pattern.search(html_text)

# Extract the matched values
if match:
    value1 = match.group(1)
    value2 = match.group(2)
    value3 = match.group(3)

    print("Value 1:", value1)
    print("Value 2:", value2)
    print("Value 3:", value3)

    # Insert the values into the PostgreSQL database
    insert_query = "INSERT INTO  regex (Value1, Value2, Value3) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (value1, value2, value3))

    # Commit the changes
    conn.commit()
    print("Values inserted into the database.")
else:
    print("No match found.")

# Close the cursor and connection
cursor.close()
conn.close()
