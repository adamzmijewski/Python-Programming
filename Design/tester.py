''' 
Created on Feb 26, 2019

@author: adamzmijewski
'''
import mysql.connector


#connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password"
  
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM kiosk.tickets")

#fetch one result
result = mycursor.fetchall()



print(result)
print('Ticket\n')

for r in result:
  
    print('Code: ',r[0])
    print('First Name: ',r[1])
    print('Last Name: ',r[2])
    print('Time: ',r[3])
    print('Date: ',r[4])
    print('Description: ',r[5],'\n\n')


code=result[0:1]
fN= result[1:2]
lN= result[2:3]
time = result[3:4]
date = result[4:5]
description = result[5:6]




#print(result)


        
        


    
    









    
    
   
     
    