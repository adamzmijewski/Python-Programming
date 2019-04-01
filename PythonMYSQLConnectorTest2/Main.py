import mysql.connector
from mysql.connector.errors import Error
import random
import Ticket

# Menu function
def Menu(cursor):
    printMenu()
        
    #input
    prompt = input('Enter choice = ')
        
    while(prompt > '0' and prompt < '4'):
        
        if(prompt == '1'):   
        
            #view the ticket
            try:
                #cursor = conn.cursor()
                ticket_code =  input(str('Input Ticket No.: '))
                cursor.execute('''SELECT * FROM Ticket where Ticket_ID = '''+ticket_code)
                for row in cursor:
                    print(row)
                    
            except Error:
                print('Failed to retrieve values')
                
            finally:
                printMenu()
                
        prompt = input('Enter choice = ')
                
# Menu display
def printMenu():
    print('Full Monty Transit\n')
    print('  1)View Ticket information')
    print('  2)Reserve Ticket')
    print('  3)Add route\n')

# RANDOM TICKET NUMBER GENERATOR
ticket_ID = str(random.randint(111111, 999999))
print('Random Ticket ID generated: %s\n' % (ticket_ID))

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
    cursor = conn.cursor()
    Menu(cursor)
    cursor.execute('''

                INSERT INTO Ticket (Starting_point, Destination, First_name, Last_name, Seat, Departure_time, Arrival_time, Departure_date, Arrival_date, Ticket_ID)
                VALUES
                ('Here', 'There', 'John', 'Doe', '211', '10:00', '14:00', '03-25-2019', '03-25-2019','''+ ticket_ID +''') 

                ''')

    conn.commit()
    print("Ticket inserted.")
    
except Error:
    print("Failed to insert ticket")