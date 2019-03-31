'''
Created on Mar 24, 2019

@author: adamzmijewski
'''
import mysql.connector
from mysql.connector.errors import Error

    #connection



#    mydb = mysql.connector.connect(host="localhost",user="root",passwd="password")

#mycursor = mydb.cursor()

#dummy_ticket = Ticket()



#mycursor = mydb.cursor()




#sql = ("select * from kiosk.tickets where kiosk.tickets.code = %s ")
#holder = code,

#mycursor.execute(sql,holder)
    
#result = mycursor.fetchall()
#print(result)
    
    #print(result)
    



        
  


print('Full Monty Transit\n')
print('1)View Ticket information')
print('2)Reserve Ticket')
print('3)Add route\n')

smydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password"
  
        )

ticket_code = ''
prompt =0
#input
while(prompt>1):
    
    prompt = input('Enter choice = ')


    if(prompt== 1):   

      #view the ticket
        ticket_code =  input('Enter code: ')
    


#user_ticket = findTicket(ticket_code)

        

        mycursor = smydb.cursor()



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
    
    else:
    
                print('Invalid Input. Please Try Again')  
        
        
    
    
    
    
    
    #user_ticket = Ticket(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],[r[8],r[9])
                                                                  
    



#print('First Name: ',user_ticket.first_Name)
#print('Last Name: ',user_ticket.Last_Name)
#print('Departure Time: ',user_ticket.depart_time)
#print('Arrival Time: ',user_ticket.arrive_time)


#print('Start:  ',user_ticket.startpoint)
#print('Destination: ',user_ticket.endpoint)
#print('Seat: ',user_ticket.seat_num)

#print('Departure Date: ',user_ticket.departdate)
#print('Arrival Date: ',user_ticket.arrival_date)
        
    
        
        
    
    
    












    

       


    
        
    
    

    
    
    
    