from socket import *
from threading import Thread
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
votes = {}
class votingServer:
    def __init__(self, host, port):
        self.server_socket = socket(AF_INET,SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"Server started on {host}:{port}")

    def start(self):
        server_thread = Thread(target=self.conn, args=())
        server_thread.start()
        votingResult()
        root.mainloop()
            
    def conn(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"New connection from {client_address}")
            client_thread = Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()
            
    def handle_client(self,client_socket):
        while True:
            message = client_socket.recv(2048).decode("utf-8")
            if(len(message)>0):
                file = open("user.txt", "a")
                file.write(message)
                file.write("\n")
                file.close()
        
    
def votingResult():
    with open('voting.txt', 'r') as file: 
     for line in file:
         key, value = line.strip().split(':')
         key="Movie "+key
         value = int(value)
         votes[key] = value
    plt.clf()
    labels = list(votes.keys())
    counts = list(votes.values())
    plt.bar(labels, counts)
    plt.ylabel("Votes")
    plt.title("Voting Results")
    plt.xticks(rotation=45)
    plt.tight_layout()
    canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0)

root = Tk()
root.title("Voting Results")
option1_button = Button(root, text="Resfresh", command= votingResult,bg='#000000', fg="#FFFFFF", font=("Arial", 16))
option1_button.grid(row=2, column=0)
host = "127.0.0.1"
port = 12345
server = votingServer(host, port)
server.start()