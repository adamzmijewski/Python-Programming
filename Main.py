import mysql.connector
from mysql.connector.errors import Error
import random
import Ticket

# RANDOM TICKET NUMBER GENERATOR
ticket_ID = str(random.randint(111111, 999999))
print(ticket_ID)

# CONNECTION BLOCK
try:
    conn = mysql.connector.connect(
        user='root', 
        password='Canada1867!', 
        host='127.0.0.1',
        database='transitsystem', 
        auth_plugin = 'mysql_native_password')
    
    print("Connection Successful")
    
except ConnectionError:
    print("Failed To Connect")
    
    # INSERTION BLOCK
try:
    mycursor = conn.cursor()
    mycursor.execute('''

                INSERT INTO Ticket (Starting_point, Destination, First_name, Last_name, Seat, Departure_time, Arrival_time, Departure_date, Arrival_date, Ticket_ID)
                VALUES
                ('Here', 'There', 'John', 'Doe', '211', '10:00', '14:00', '03-25-2019', '03-25-2019','''+ ticket_ID +''') 

                ''')

    conn.commit()
    print("Ticket inserted.")
    
except Error:
    print("Failed to insert ticket")
   
# RETRIEVAL/PRINT BLOCK    
try:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Ticket')
    for row in cursor:
        print(row)
    
except Error:
    print('Failed to retrieve values')