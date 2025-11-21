import sqlite3

# Connect to the database (it will create it if it doesn't exist)
connection = sqlite3.connect('livingwithmama.db')

# Read your schema.sql file
with open('schema.sql') as f:
    connection.executescript(f.read())

# Save and close
connection.commit()
connection.close()

print("Success! Database created.")