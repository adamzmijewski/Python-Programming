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
        
    def set_Starting_point(self, location):
        self.Starting_point = location
        
    def set_Destination(self, location):
        self.Destination = location
      
    def set_First_name(self, name):
        self.First_name = name
        
    def set_Last_name(self, name):
        self.Last_name = name
        
    def set_Seat(self, seat):
        self.Seat = seat
        
    def set_Departure_time(self, time):
        self.Departure_time = time
        
    def set_Arrival_time(self, time):
        self.Arrival_Time = time
        
    def set_Departure_date(self, date):
        self.Departure_date = date
        
    def set_Arrival_date(self, date):
        self.Arrival_date = date
        
    def set_Ticket_ID(self, ID):
        self.Ticket_ID = ID
        
    