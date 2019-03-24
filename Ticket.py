class Ticket:
    Ticket_ID = 0
    Starting_Point = ''
    Destination = ''
    Departure_Time = 0
    Arrival_Time = 0
    
    def Ticket(self, Ticket_ID, Starting_point, Destination, Departure_Time, Arrival_Time):
        self.Ticket_ID = Ticket_ID
        self.Starting_Point = Starting_point
        self.Destintion = Destination
        self.Departure_Time=  Departure_Time
        self.Arrival_Time = Arrival_Time
        
    def set_Ticket_ID(self, ID):
        self.Ticket_ID = ID
        
    def set_Starting_Point(self, location):
        self.Starting_Point = location
        
    def set_Destination(self, location):
        self.Destination = location
        
    def set_Departure_Time(self, time):
        self.Departure_Time = time
        
    def set_Arrival_Time(self, time):
        self.Arrival_Time = time
        
    