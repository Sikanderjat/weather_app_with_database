import pymysql

# Connection details from the public URL
connection = pymysql.connect(
    host="autorack.proxy.rlwy.net",   # The host from the URL
    user="root",                       # The username from the URL
    password="GAwTGAJoogDQLKUdzYOrSMhCdpTwRcGg",  # The password from the URL
    database="railway",                # The database from the URL
    port=50724                         # The port from the URL
)

try:
    with connection.cursor() as cursor:
        # Check if the 'signup' table exists
        cursor.execute("SHOW TABLES LIKE 'signup'")
        table_exists = cursor.fetchone()

          
        print("Table 'signup' doesn't exist. Creating it now.")
        create_table_query = """
        CREATE TABLE signup (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL,
            con_password VARCHAR(100) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor.execute(create_table_query)
        print("Table 'signup' created successfully.")

        # Now, query the 'signup' table for data
        cursor.execute("SELECT * FROM signup")
        results = cursor.fetchall()
        if results:
            print("Data in 'signup' table:")
            for row in results:
                print(row)
        else:
            print("No data found in the 'signup' table.")


except Exception as e:
    print("Error connecting to the database:", e)
finally:
    connection.close()
