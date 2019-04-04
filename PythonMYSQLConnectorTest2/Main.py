import mysql.connector
from mysql.connector.errors import Error
import random
from Ticket import Ticket

new_ticket = Ticket()

# Menu function
def Menu(cursor, new_ticket):
    printMenu()
        
    #input
    prompt = input('Enter choice:')
    print()
        
    while(prompt > '0' and prompt < '4'):
        
        if(prompt == '1'):   
        
            #view the ticket
            try:
                #cursor = conn.cursor()
                ticket_code =  input(str('Input Ticket Number: '))
                print()
                cursor.execute('''SELECT * FROM Ticket where Ticket_ID = '''+ticket_code)
                print('\nTICKET INFO:', end = ' ')
                for row in cursor:
                    print(row)
                    
            except Error:
                print('Failed to retrieve values')
                
            finally:
                printMenu()
                prompt = input('Enter choice = ')

        elif prompt == '2':
            new_ticket.set_Starting_point(input('Enter Starting Point:'))
            new_ticket.set_Destination(input('Enter Destination:'))
            new_ticket.set_First_name(input('Enter Passenger First Name:'))
            new_ticket.set_Last_name(input('Enter Passenger Last Name:'))
            new_ticket.set_Seat(input('Choose Seat:'))
            new_ticket.set_Departure_time(input('Enter Departure Time:'))
            new_ticket.set_Arrival_time(input('Enter Arrival Time:'))
            new_ticket.set_Departure_date(input('Enter Departure Date:'))
            new_ticket.set_Arrival_date(input('Enter Arrival Date:'))
            new_ticket.set_Ticket_ID(str(generateTicketID()))

            try:
                sql_insert_query = '''
    
                                INSERT INTO Ticket (Starting_point, Destination, First_name, Last_name, Seat, 
                                                    Departure_time, Arrival_time, Departure_date, Arrival_date, Ticket_ID)
                                VALUES
                                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

                insert_tuple = (new_ticket.get_Starting_point(),
                                new_ticket.get_Destination(),
                                new_ticket.get_First_name(),
                                new_ticket.get_Last_name(),
                                new_ticket.get_Seat(),
                                new_ticket.get_Departure_time(),
                                new_ticket.get_Arrival_time(),
                                new_ticket.get_Departure_date(),
                                new_ticket.get_Arrival_date(),
                                new_ticket.get_Ticket_ID())

                result = cursor.execute(sql_insert_query, insert_tuple)
                conn.commit()
                print("Ticket created.  Ticket ID is %s\n" % (new_ticket.get_Ticket_ID()))

            except Error:
                print('Ticket Not Inserted')

            finally:
                printMenu()
                prompt = input('Enter choice = ')
        
        elif prompt == '3':
            pass
                
                       
    print("System Exited.\n")
                
# Menu display
def printMenu():
    print('\nFull Monty Transit')
    print('  1)View Ticket information')
    print('  2)Reserve Ticket')
    print('  3)Add route\n')

# RANDOM TICKET NUMBER GENERATOR
def generateTicketID():
    return str(random.randint(111111, 999999))

#ticket_ID = generateTicketID()
#print('Random Ticket ID generated: %s\n' % (ticket_ID))

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
    Menu(cursor, new_ticket)
    
except Error:
    print("Failed to insert ticket")
    
finally:
    conn.close()