import mysql.connector  # Import the MySQL connector module

def connect_to_db():
    """
    Establish a connection to the MySQL database.

    Returns:
        A connection object to interact with the database.
    """
    connection = mysql.connector.connect(
        host='localhost',         # MySQL server address (localhost if running locally)
        user='username',              # Your MySQL username
        password='your-pass',      # Your MySQL password
        database='test'           # The name of the database you want to connect to
    )
    return connection

def find_user_by_username(cursor, username):
    """
    Search for a user by their username in the 'users' table.

    Args:
        cursor: A MySQL cursor object used to execute queries.
        username (str): The username to search for.

    Returns:
        Prints the user details if found, otherwise prints a not found message.
    """
    try:
        # Use a parameterized query to prevent SQL injection
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()

        if result:
            print('✅ User found:', result)
        else:
            print("❌ User not found.")

    except mysql.connector.Error as e:
        print(f"⚠️ Database error: {e}")

if __name__ == "__main__":
    # Prompt the user for a username
    username = input("Enter username: ")

    # Connect to the database
    conn = connect_to_db()
    cursor = conn.cursor()

    # Search for the user
    find_user_by_username(cursor, username)

    # Close the cursor and connection to release resources
    cursor.close()
    conn.close()