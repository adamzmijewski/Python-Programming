'''
Created on Apr 2, 2019
@author: adamzmijewski'''
class Route(object):


    def __init__(self, id,routeNumber,passengers,startpoint,endpoint,time,duration):
        self.id = id
        self.routeNumber=routeNumber
        self.passengers=passengers
        self.startpoint=startpoint
        self.endpoint=endpoint
        self.time=time
        self.duration=duration
