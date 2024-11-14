import pandas as pd
import mysql.connector

# Database configuration
db_config = {
    'user': 'db_user',
    'password': 'db_password',
    'host': 'localhost',
    'database': 'mydatabase'
}

def upload_csv_to_mysql(csv_file, table_name):
    # Load CSV file
    data = pd.read_csv(csv_file)

    # Connect to MySQL
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # SQL query to insert data
    insert_query = f"""
    INSERT INTO {table_name} (
        Game_Title, User_Rating, Age_Group_Targeted, Price, Platform,
        Requires_Special_Device, Developer, Publisher, Release_Year, Genre,
        Multiplayer_Game, Length_Hours, Graphics_Quality, Soundtrack_Quality,
        Story_Quality, User_Review_Text, Game_Mode, Min_Number_of_Players
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Insert each row into the MySQL table
    for _, row in data.iterrows():
        cursor.execute(insert_query, (
            row['Game_Title'], row['User_Rating'], row['Age_Group_Targeted'], row['Price'], row['Platform'],
            row['Requires_Special_Device'], row['Developer'], row['Publisher'], row['Release_Year'], row['Genre'],
            row['Multiplayer_Game'], row['Length_Hours'], row['Graphics_Quality'], row['Soundtrack_Quality'],
            row['Story_Quality'], row['User_Review_Text'], row['Game_Mode'], row['Min_Number_of_Players']
        ))

    # Commit the transaction
    conn.commit()
    print("Data uploaded successfully")

    # Close the connection
    cursor.close()
    conn.close()

# Use the function to upload CSV data
upload_csv_to_mysql('video.csv', 'video_game')
