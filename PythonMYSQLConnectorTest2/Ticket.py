class Ticket:

    @property
    def __init__(self, Starting_point, Destination, First_name, Last_name, Seat, 
               Departure_Time, Arrival_Time, Departure_date, Arrival_date, Ticket_ID):
        self.Starting_Point = Starting_point
        self.Destintion = Destination
        self.First_name = First_name
        self.Last_name = Last_name
        self.Seat = Seat
        self.Departure_Time=  Departure_Time
        self.Arrival_Time = Arrival_Time
        self.Departure_date = Departure_date
        self.Arrival_date = Arrival_date
        self.Ticket_ID = Ticket_ID
    
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
        self.First_name = name
        
    def get_First_name(self):
        return self.First_name
    
    
    # Set/Get for Last_name
    def set_Last_name(self, name):
        self.Last_name = name
        
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
        
        
    # Set/Get for Arrival_time
    def set_Arrival_time(self, time):
        self.Arrival_Time = time
        
    def get_Arrival_time(self):
        return self.Arrival_time
        
        
    # Set/Get for Departure_date
    def set_Departure_date(self, date):
        self.Departure_date = date
        
    def get_Departure_date(self):
        return self.Departure_date
        
        
    # Set/Get for Arrival_date
    def set_Arrival_date(self, date):
        self.Arrival_date = date
        
    def get_Arrival_date(self):
        return self.Arrival_date
        
        
    # Set/Get for Ticket_ID
    def set_Ticket_ID(self, ID):
        self.Ticket_ID = ID
        
    def get_Ticket_ID(self):
        return self.Ticket_ID
        
    