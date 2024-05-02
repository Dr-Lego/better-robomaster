import socket


class Connection(object):
    def __init__(self, host: str = "192.168.2.1", port: int = 40923) -> None:
        # In direct connection mode, the default IP address of the robot is 192.168.2.1 and the control command port is port 40923.
        self.host: str = host
        self.port: int = host
        self.address: tuple = (host, int(port))
        self.socket: socket.socket

    def connect(self):
        # Establish a TCP connection with the control command port of the robot.
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Connecting...")
        self.socket.connect(self.address)
        print("Connected!")

    def send(self, msg: str):
        # Send control commands to the robot.
        self.socket.send(msg.encode('utf-8'))
        # Wait for the robot to return the execution result.
        buf = self.socket.recv(1024)

        return buf.decode('utf-8')
    
    def disconnect(self):
        # Disconnect the port connection.
        self.socket.shutdown(socket.SHUT_WR)
        self.socket.close()
