import sqlite3

# Function to create a table
def create_table():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    # Create the table with appropriate column names and data types
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    phone TEXT)''')

    conn.commit()
    conn.close()

# Function to update a table
def update_contact(id, name, phone):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    # Execute the update query
    cursor.execute('UPDATE contacts SET name=?, phone=? WHERE id=?', (name, phone, id))

    conn.commit()
    conn.close()

# Function to delete from a table
def delete_contact(id):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    # Execute the delete query
    cursor.execute('DELETE FROM contacts WHERE id=?', (id,))

    conn.commit()
    conn.close()

# Function to insert into a table
def insert_contact(name, phone):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    # Execute the insert query
    cursor.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))

    conn.commit()
    conn.close()

# Function to read (load in) record(s) from a table
def read_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    # Execute the select query to retrieve all records
    cursor.execute('SELECT * FROM contacts')

    contacts = cursor.fetchall()  # Fetch all records

    conn.close()

    return contacts

# Call the create_table() function to ensure the table is created
create_table()
