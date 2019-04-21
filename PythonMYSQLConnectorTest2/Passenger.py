#AUTHORS: Jeff Hall
#PURPOSE: Passenger Class - Acts As Base Class For Ticket Class
#CREATION DATE: March 30, 2019
#LAST MODIFICATION DATE: April 14, 2019
class Passenger(object):
    
#Constructor
    def __init__(self):
        self.first_name = ""
        self.last_name = ""