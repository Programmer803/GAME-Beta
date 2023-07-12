import socket
import time
import random

class Server:

    def __init__(self):

        self.speed = 4
        self.level = 1

        self.start = True
        self.play = True


        self.ip_list = []
        self.rr = []
        self.usernames = []
        self.sock = socket.socket()
        self.ip = input("Ip: ")
        self.port = input("Port: ")
        self.bind_()
        

    def bind_(self):
        
        self.sock.bind((self.ip,int(self.port)))
        self.sock.listen(2)
        self.addr , self.g = self.sock.accept()
        self.ip_list.append(self.g)
        self.rr.append(self.addr)

    def rand(self):
            

            x = int(random.choice(["-1","1"]))

            y = int(random.choice(["-1","1"]))

            return (x*self.speed, y*self.speed)

    def connect(self):
            
            self.level += 1
            
            msg = str(self.addr.recv(1024).decode())

            self.message = msg.split(" ")

            if self.play == True:

                l = ["L","R"]

                

                for net in self.rr:
                     
                     r = random.choice(l)
                     
                     net.send(str("PL: "+r+" ** ").encode())
                     ind = l.index(r)
                     del l[ind]

                self.play = False
                     
                
                 
                
            if self.start == True:
                

                for net in self.rr:
                      
                      net.send(str("ST: "+str(self.rand()[0])+" "+str(self.rand()[1])+" ** ").encode())
                      self.start = False

            if self.message[0] == "SS:":
                 
                 for net in self.rr:
                      
                      net.send(str("B: ** ").encode())    

                 self.start = True     
        
            if self.level == 50:
                 
                 self.speed_ = (self.speed * 3) / 2
                 
                 for net in self.rr:
                      
                      net.send(str("S: "+str(self.speed_)+" ** ").encode())

            if self.message[0] == "U:":

                self.usernames.append(self.message[1])
            
            elif self.message[1] == "M:":
                 
                i = self.usernames.index(self.message[0])
                try:
                      
                    self.rr[0].send(str(self.message[0]+" M: "+self.message[3]+" ** ").encode())

                except:
                     print("E")




            
            

        
        

server = Server()
while 1:
     server.connect()
