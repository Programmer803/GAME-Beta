import socket
import time
import _thread
from main import Game

my_game = Game()

sock  = socket.socket()

class online_game(Game):

    def __init__(self):

        Game.__init__(self)

        self.sock = sock
        self.pack = None
        self.packets =[]
        

    def send(self , msg):

        self.sock.send(str(msg).encode())

    def send_m(self , msg):

        self.sock.send(str(self.username+" M: "+msg).encode())
    
    def connect(self):
        
        self.username = input("Username: ")

        self.ip = input("Ip: ")

        self.port = input("Port: ")

        try:

            self.sock.connect((self.ip,int(self.port)))

            self.send("U: "+self.username)

        except:

            pass


    def finder(self):
         
         count = list(self.pack).count("**")

         for _ in range(count):
              
              f = list(self.pack).index("**")
              self.packets.append(self.pack[0:f])
              del self.pack[0:f+1]
         

    def reccv(self):
            

        
            self.send_m(" " +str(my_game.palyer_addr[1]))

            self.msg = self.sock.recv(1024).decode()
           
            
            self.msg = self.msg.split(" ")
            self.pack = self.msg
            
            time.sleep(0.01)

            self.finder()

           

            for d in self.packets:
                print(d)
                 

                if d[0] == "PL:":
                    
                    if d[1] == "R":
                        
                        my_game.player = "R"

                    else:
                         my_game.player = "L"
                        


                if d[0] == "ST:":
                    
                    my_game.ball_move = (int(d[1]),int(d[2]))


                if d[0] == "B:":

                    my_game.ball_addr = self.d_ball_addr

       

                if d[0] == "S:" :

                    my_game.f_speed == float(d[1])


                if my_game.ball_addr[0] <= 22:
                        
                        self.send("SS: "+self.username)
                    

                elif my_game.ball_addr[0] >= 781:
                        
                        self.send("SS: "+"Other")

                if d[1] == "M:" and d[0] != self.username:

                    return d[3]
                
            # del self.packets[0::]
                


    


on_line = online_game()

on_line.connect()




while True:

    my_game.main()    

    on_line.reccv()

        