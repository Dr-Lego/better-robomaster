from . import Connection

class Robot(object):
    def __init__(self) -> None:
        self.connnection = Connection()
        
    def connect(self) -> None:
        self.connnection.connect()
        
    def disconnect(self) -> None:
        self.connnection.disconnect()
    
    def battery(self) -> int:
        return self.connnection.send("robot battery ?;")
    
    def move(self, x:float=0, y:float=0, rotation:float=0) -> None:
        if x < -5 or x > 5:
            raise ValueError("The x-axis movement distance in meters has to be in range [-5; 5]")
        elif y < -5 or y > 5:
            raise ValueError("The y-axis movement distance in meters has to be in range [-5; 5]")
        elif rotation < -1800 or rotation > 1800:
            raise ValueError("The z-axis rotation angle in degrees has to be in range [-1800; 1800]")
        return self.connnection.send(f"chassis move x {x} y {y} z{rotation}")