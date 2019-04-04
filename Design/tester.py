''' 
Created on Feb 26, 2019

@author: adamzmijewski


'''

#imports
import mysql.connector
from mysql.connector.errors import Error
from Route import Route
        
#ticket_code =  input('Enter code: ')

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password"
  
        )



routeid = input("Enter the ID: ")
routeNumber =input("Enter the route number: ")
passengers = input("Enter the number of passengers: ")
startpoint = input("Enter a starting point: ")
endpoint = input("Enter a end point: ")
time = input("Enter the starting time: ")
duration = input("Enter the duration: ")

#make the object

userRoute = Route(routeid,routeNumber,passengers,startpoint,endpoint,time,duration)

#insert statement

try:
     
    #connect
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password"
  
        )
    
    print("Connection Successful")
    
except ConnectionError:
    print("Failed To Connect")
    
    # INSERTION BLOCK
try:
    cursor = conn.cursor()
    #Menu(cursor)
   # mysqlInsert = ('INSERT INTO kiosk.route (id, route_number, passengers, starting_point, end_point, time, duration)VALUES(%s, %s, %s, %s, %s, %s, %s)', (userRoute.id,userRoute.routeNumber,userRoute.passengers,userRoute.startpoint,userRoute.endpoint,userRoute.time,userRoute.duration) 
    
    sql_insert_query = """INSERT INTO  kiosk.route (id, route_number, passengers, starting_point,end_point,time,duration) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    
    #INSERT INTO  kiosk.route (id, route_number, passengers, starting_point,end_point,time,duration) VALUES (1,'dfasfd','dfasfd','dfasfd','dfasfd','dfasfd','dfasfd')
    varz = (userRoute.id,userRoute.routeNumber,userRoute.passengers,userRoute.startpoint,userRoute.endpoint,userRoute.time,userRoute.duration)
    
    #print(varz)
    
    result = cursor.execute(sql_insert_query,varz)
    conn.commit()
    print("Route inserted successfully.")
    
except Error:
    print("Failed to insert route")


'''
mycursor = mydb.cursor()

sql = ("select * from kiosk.tickets where kiosk.tickets.code = %s ")
holder = ticket_code,

mycursor.execute(sql,holder)
    
result = mycursor.fetchall()
print(result)

for r in result:
    
    print ('Code: ',  r[0])
    print('First Name: ',r[1])
    print('Last Name: ',r[2])
    print('Departure Time: ', r[3])
    print('Arrival Time: ',r[4])


    print('Start:  ',r[5])
    print('Destination: ',r[6])
    print('Seat: ',r[7])

    print('Departure Date: ',r[8])
    print('Arrival Date: ',r[9])

#class work

import os


myfile=open('march28.txt')
content = myfile.read()
myfile.close()

print(content)




spaces =0
lines =0 
characters = 0        
 
for i in content:                 
    
    
    
    
    #cases
    
    #check spaces
    if(i == " "):
        spaces += 1
    #check lines
    elif(i == "\n"):
        lines += 1
    #check characters
    else:
        characters += 1


print('Number of characters: ',characters)


'''









































        
        


    
    









    
    
   
     
    