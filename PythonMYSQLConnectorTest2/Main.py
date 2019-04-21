import mysql.connector
from mysql.connector.errors import Error
import random
from Ticket import Ticket  #TICKET CLASS CREATED FOR PROJECT
from Route import Route    #ROUTE CLASS CREATED FOR PROJECT

#GLOBAL VARIABLE - NEW TICKET TO BE INSERTED
new_ticket = Ticket()

#AUTHORS: Jeff Hall, Adam Zmijewski
#PURPOSE: Manages Menu Option Operations:
#         1) Searches Database For Ticket Info;
#         2) Books New Ticket Into Database
#         3) Adds Route TO Db, If Logged In As Administrator
#CREATION DATE: March 30, 2019
#LAST MODIFICATION DATE: April 14, 2019
#INPUT: MySQL Cursor object, Ticket Object
#OUTPUT: None 
def Menu(cursor, new_ticket):
    printMenu()
        
    # input
    prompt = input('Enter choice:')
    print()
        
    while(prompt > '0' and prompt < '4'):
        
        if(prompt == '1'):   
        
            # view the ticket
            try:
                ticket_code = input(str('Input Ticket Number: '))
                print()

                # Print Ticket Info
                cursor.execute('''SELECT * FROM tickets where code = '''+ticket_code)
                print('\n  TICKET INFO: Ticket #   First Name   Last Name   Leaving At     '
                      'From          To          Seat      Trip Date')
                for row in cursor:
                    print('               ', end='')
                    for i in range(0, 8):
                        print(row[i], end='       ')
                print()
                    
            except Error:
                print('Failed to retrieve values')
                
            finally:
                printMenu()
                prompt = input('Enter choice = ')
        #Book A New Trip
        elif prompt == '2':
            valid_trip = validateTrip(new_ticket)

            while valid_trip == False:
                valid_trip = validateTrip(new_ticket)
            
            #Save Input As New Ticket Object
            new_ticket.set_First_name(input('Enter Passenger First Name:'))
            new_ticket.set_Last_name(input('Enter Passenger Last Name:'))
            new_ticket.set_Seat(input('Choose Seat:'))
            new_ticket.set_Departure_time(input('Enter Departure Time:'))
            new_ticket.set_Departure_date(input('Enter Departure Date:'))
            new_ticket.set_Ticket_ID(str(generateTicketID()))
            
            #Insert New Ticket Into Database
            try:
                sql_insert_query = '''
    
                                INSERT INTO tickets (code, first_name, last_name, depart_time, startpoint, 
                                                    endpoint, seat_num, depart_date)
                                VALUES
                                (%s,%s,%s,%s,%s,%s,%s,%s)'''

                insert_tuple = (new_ticket.get_Ticket_ID(),
                                new_ticket.get_First_name(),
                                new_ticket.get_Last_name(),
                                new_ticket.get_Departure_time(),
                                new_ticket.get_Starting_point(),
                                new_ticket.get_Destination(),
                                new_ticket.get_Seat(),
                                new_ticket.get_Departure_date())

                cursor.execute(sql_insert_query, insert_tuple)
                conn.commit()

                # Write New Ticket To .txt File
                writeToFile(insert_tuple)

                update_sql = 'update kiosk.route set kiosk.route.Id = kiosk.route.Id + 1 ' \
                             'where kiosk.route.starting_point = %s and kiosk.route.end_point = %s'
                update_holder = (new_ticket.get_Starting_point(), new_ticket.get_Destination())
                cursor.execute(update_sql, update_holder)
                conn.commit()

                print("\nTicket created.  Ticket ID is %s\n" % (new_ticket.get_Ticket_ID()))

            except Error:
                print('Ticket Not Inserted')

            finally:
                printMenu()
                prompt = input('Enter choice = ')
        
        #Add New Route To Database
        elif prompt == '3':
            #username = 'root' | password = 'password'
            print('Add a new Route')
            username = input("Enter your user name: ")
            password = input("Enter password: ")

            if (username == 'root' and password == 'password'):
                routeid = 0
                routeNumber = input("Enter the route number: ")
                passengers = input("Enter the number of passengers: ")
                startpoint = input("Enter a starting point: ")
                endpoint = input("Enter a end point: ")
                time = input("Enter the starting time: ")
                duration = input("Enter the duration: ")

                #Save Input As Route Object
                userRoute = Route(routeid, routeNumber, passengers, startpoint, endpoint, time, duration)

                #Insert New Route To Database
                try:
                    sql_insert_query = """INSERT INTO  kiosk.route (id, route_number, passengers, starting_point,
                                          end_point,time,duration) VALUES (%s,%s,%s,%s,%s,%s,%s)"""

                    varz = (
                    userRoute.id, userRoute.routeNumber, userRoute.passengers, userRoute.startpoint, userRoute.endpoint,
                    userRoute.time, userRoute.duration)

                    cursor.execute(sql_insert_query, varz)
                    conn.commit()
                    print("Route inserted successfully.")

                except Error:
                    print("Failed to insert route")

                finally:
                    printMenu()
                    prompt = input('Enter choice = ')

            else:
                print("Access Denied\n")
                printMenu()
                prompt = input('Enter choice = ')

    print("System Exited.\n")
                
#AUTHORS: Jeff Hall, Adam Zmijewski
#PURPOSE: Prints Menu Options 
#CREATION DATE: March 30, 2019
#LAST MODIFICATION DATE: April 14, 2019
#INPUT: None
#OUTPUT: None 
def printMenu():
    print('\nFull Monty Transit')
    print('  1)View Ticket information')
    print('  2)Reserve Ticket')
    print('  3)Add route\n')


#AUTHORS: Jeff Hall, Adam Zmijewski
#PURPOSE: Recursive Random Integer Function - Added To Ticket ID Number
#CREATION DATE: March 30, 2019
#LAST MODIFICATION DATE: April 14, 2019
#INPUT: None
#OUTPUT: Random 6-Digit Integer
def generateTicketID():
    temp = random.randint(1, 5)
    return str(factorialTicketID(temp) + random.randint(111111, 999999))

#AUTHORS: Adam Zmijewski
#PURPOSE: Generates Random 6-Digit Ticket ID Number, Between 111111 And 999999
#CREATION DATE: March 30, 2019
#LAST MODIFICATION DATE: April 14, 2019
#INPUT: None
#OUTPUT: Random 6-Diget Integer
def factorialTicketID(num):
    if num == 1:
        return 1
    else:
        return (num*factorialTicketID(num-1))
    
#AUTHORS: Jeff Hall, Adam Zmijewski
#PURPOSE: Validates Starting Point And Destination of Proposed Trip - And If Seats Available
#CREATION DATE: March 30, 2019
#LAST MODIFICATION DATE: April 14, 2019
#INPUT: Ticket Object From Imported Ticket Class
#OUTPUT: BOOLEAN - Returns True if Locations Valid And Tickets Available,
#                  Returns False If Any Of The Above Are Invalid
def validateTrip(new_ticket):
    try:
        #Sets Input TO Lower case, To Match Database LocationEntries
        new_ticket.set_Starting_point(input('Enter Starting Point:').lower())
        new_ticket.set_Destination(input('Enter Destination:').lower())
        
        #Selects Starting Points, Destinations, And Tickets Available From DB
        sql = (
            "select kiosk.route.starting_point, kiosk.route.end_point, kiosk.route.passengers, kiosk.route.Id, "
            "kiosk.route.time from kiosk.route where kiosk.route.starting_point = %s and kiosk.route.end_point = %s")
        
        holder2 = (new_ticket.get_Starting_point(), new_ticket.get_Destination())
        cursor.execute(sql, holder2)
        result = cursor.fetchone()
        maxSeats = int(result[2])
        
        #Invalidates Trip If Train Is Full, Or Locations Do Not Exist 
        if result[0] == new_ticket.get_Starting_point() and result[1] == new_ticket.get_Destination():
            if result[3] >= maxSeats:
                print('Sorry no tickets left. Please try another selection.')
                return False
            print('A route has been found matching the criteria.')
            print("%d seats left.  Enter info to book." % (maxSeats - result[3]))
            return True

        else:
            update_cursor = conn.cursor()

            update_sql = 'update kiosk.route set kiosk.route.Id = kiosk.route.Id + 1 ' \
                         'where kiosk.route.starting_point = %s and kiosk.route.end_point = %s'

            update_holder = (new_ticket.get_Starting_point(), new_ticket.get_Destination())

            update_cursor.execute(update_sql, update_holder)

            conn.commit()

            return True

    except TypeError:
        print('Invalid selection')
        return False

#AUTHORS: Jeff Hall, Adam Zmijewski
#PURPOSE: Writes New Ticket Info To .txt File
#CREATION DATE: March 30, 2019
#LAST MODIFICATION DATE: April 14, 2019
#INPUT: Tuple Consisting Of All Individual New Ticket Info
#OUTPUT: None 
def writeToFile(tuple):
    file = open('tickets.txt', 'a')
    file.write(" ".join(tuple))
    file.write('\n')
    file.close()

#DB CONNECTION BLOCK
try:
    conn = mysql.connector.connect(
    user='root', 
    password='Canada1867!', 
    host='127.0.0.1',
    database='kiosk',
    auth_plugin='mysql_native_password')
    
    print("Connection Successful")
    
except ConnectionError:
    print("Failed To Connect")
    
    #INSERTION BLOCK
try:
    cursor = conn.cursor()    #Creates New SQL Cursor Object
    Menu(cursor, new_ticket)  #Call To Menu Function - Passes Cursor and Global Ticket Objects
    
except Error:
    print("Failed to insert ticket")
    
finally:
    conn.close()
