#AUTHORS: Jeff Hall
#PURPOSE: Ticket Class For All Information 
#          On Newly Created Ticket
#CREATION DATE: March 30, 2019
#LAST MODIFICATION DATE: April 14, 2019
from Passenger import Passenger

class Ticket(Passenger):  #Inherits from Passenger Class

#Constructor
    def __init__(self):
        self.Starting_Point = ''
        self.Destination = ''
        self.Seat = ''
        self.Departure_time = ''
        self.Departure_date = ''
        self.Ticket_ID = ''
    
    # Set/Get for Starting_point
    def set_Starting_point(self, location):
        self.Starting_point = location
        
    def get_Starting_point(self):
        return self.Starting_point
        
        
    # Set/Get for Destination
    def set_Destination(self, location):
        self.Destination = location
        
    def get_Destination(self):
        return self.Destination
      
      
    # Set/Get for First_name
    def set_First_name(self, name):
        #Calls Constructor For Base Class
        Passenger.First_name = name
        
    def get_First_name(self):
        return self.First_name
    
    
    # Set/Get for Last_name
    def set_Last_name(self, name):
        #Calls Constructor For Base Class
        Passenger.Last_name = name
        
    def get_Last_name(self):
        return self.Last_name
    
    
    # Set/Get for Seat  
    def set_Seat(self, seat):
        self.Seat = seat
        
    def get_Seat(self):
        return self.Seat
    
    
    # Set/Get for Departure_time
    def set_Departure_time(self, time):
        self.Departure_time = time
        
    def get_Departure_time(self):
        return self.Departure_time
        
        
    # Set/Get for Departure_date
    def set_Departure_date(self, date):
        self.Departure_date = date
        
    def get_Departure_date(self):
        return self.Departure_date
        
        
    # Set/Get for Ticket_ID
    def set_Ticket_ID(self, ID):
        self.Ticket_ID = ID
        
    def get_Ticket_ID(self):
        return self.Ticket_ID

