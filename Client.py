import tkinter as tk
from socket import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

serverIP = "127.0.0.1"
serverPort = 12345
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))
def SignUp():
   try:
    def printt():
         name=username_entry.get()
         pas=password_entry.get()
         sentence = name + "," +pas
         clientSocket.send(bytes(sentence,"utf-8"))
         username_entry.delete(0, END)
         password_entry.delete(0, END)
         Voter(name,pas,root)

        
    root1.destroy()
    root = Tk()
    root.title("Sign Up")
    root.geometry('800x600')
    root.configure(bg='#000000')
    frame = Frame(bg='#000000')
    img=Image.open('images\smile.png')
    resized= img.resize((200,350))
    test = ImageTk.PhotoImage(resized)
    label=Label(root,image=test,bg='black').place(x=20,y=20,width=200,height=600)
 
    signup_label = Label(frame, text="Sign Up", bg='#000000', fg="#FA2A2A", font=("Arial", 50))
    username_label = Label(frame, text="username", bg='#000000', fg="#FFFFFF", font=("Arial", 16))
    username_entry = Entry(frame, font=("Arial", 16))
    username_entry = Entry(frame, font=("Arial", 16))
    password_entry = Entry(frame, show="*", font=("Arial", 16))
    password_label = Label(frame, text="Password", bg='#000000', fg="#FFFFFF", font=("Arial", 16))
    login_button = Button(frame,command=printt, text="Sign Up", bg="#FFFFFF", fg="#FA2A2A", font=("Arial", 16,"bold"),padx=15,pady=10)
  
    signup_label.grid(row=0, column=2, columnspan=3, sticky="news", pady=40)
    username_label.grid(row=1, column=1)
    username_entry.grid(row=1, column=2, pady=20)
    password_label.grid(row=2, column=1)
    password_entry.grid(row=2, column=2, pady=20)
    login_button.grid(row=5, column=1, columnspan=2, pady=30)
    frame.pack()
    root.mainloop() 
   except:
       pass
 
def checkUser():
   try:
       file = open("votedUsers.txt", "r")
       Lines = file.readlines()
       file.close()
       for line in Lines:
           msg = list(map(str.strip, line.split(',')))
           if ((numenter1.get()==msg[0]) & (numenter2.get()==msg[1])):
               numlable5['text'] ="You Voted 2bl keda Mt2rfnash"
               numenter1.delete(0, END)
               numenter2.delete(0, END)
           else:
             continue 
       file = open("user.txt", "r")
       Lines = file.readlines()
       file.close()
       for line in Lines:
         msg = list(map(str.strip, line.split(',')))
         if ((numenter1.get()==msg[0]) & (numenter2.get()==msg[1])):
             Voter(numenter1.get(),numenter2.get(),root1)
         else:
             continue 
       numlable5['text'] ="Invalid Username Or Password !!"
   except:
       pass
def Voter(user,password,root1):
    root1.destroy()
    vote = Tk()
    try:
       myvar=IntVar()
    except:
        pass
    def Vote():
        number=myvar.get()
        if number==0:
          messagebox.showwarning("Warning !","Please, Vote !!!")
        else:
          x= messagebox.askokcancel("Warning !","Do you want to submit your voting?")
          if x:
              vote.destroy()
              file = open("voting.txt", "r")
              Lines = file.readlines()
              file.close()
              open('voting.txt', 'w').close()
              file = open("voting.txt", "a")
              for line in Lines:
                  msg = list(map(str.strip, line.split(':')))
                  num=int(msg[1])
                  if int(msg[0]) == number:
                      num=num+1
                  file.write(msg[0])
                  file.write(":")
                  file.write(str(num))
                  file.write("\n")
              file.close()
              file = open("votedUsers.txt", "a")
              file.write(user)
              file.write(",")
              file.write(password)
              file.write("\n")
              file.close()
               
    vote.geometry("800x600")
    vote.title("Voting")
    lbl=Label(vote,text="All these movies based on real-life events, Choose your fav",font=('Ink Free',20),pady="10",fg="Red",bg="black")
    lbl.pack()
    image = Image.open("images\Annabelle.jpg")
    resized= image.resize((180,220))
    test = ImageTk.PhotoImage(resized)
    img = Label(image=test)
    img.image = test
    img.place(x=25, y=50)
    btn=Radiobutton(vote,text="Annabelle",value=1,font=('Ink Free',12),fg="Red",bg="black",variable=myvar)
    btn.pack()
    btn.place(x=35,y=275)
   
    image = Image.open("images\TheConjuring.jpg")
    resized= image.resize((180,220))
    test = ImageTk.PhotoImage(resized)
    img = Label(image=test)
    img.image = test
    img.place(x=215, y=50)
    btn=Radiobutton(vote,text="The Conjuring",value=2,font=('Ink Free',12),fg="Red",bg="black",variable=myvar)
    btn.pack()
    btn.place(x=225,y=275)

    image = Image.open("images/rite.jpg")
    resized= image.resize((180,220))
    test = ImageTk.PhotoImage(resized)
    img = Label(image=test)
    img.image = test
    img.place(x=405, y=50)
    btn=Radiobutton(vote,text="RITE",value=3,font=('Ink Free',12),fg="Red",bg="black",variable=myvar)
    btn.pack()
    btn.place(x=415,y=275)
    
    image = Image.open("images\cild'splay.jpg")
    resized= image.resize((180,220))
    test = ImageTk.PhotoImage(resized)
    img = Label(image=test)
    img.image = test
    img.place(x=595, y=50)
    btn=Radiobutton(vote,text="Cild's Play",value=4,font=('Ink Free',12),fg="Red",bg="black",variable=myvar)
    btn.pack()
    btn.place(x=605,y=275)
    
    image = Image.open("images/theExorcism.jpg")
    resized= image.resize((180,220))
    test = ImageTk.PhotoImage(resized)
    img = Label(image=test)
    img.image = test
    img.place(x=25, y=300)
    btn=Radiobutton(vote,text="The Exorcism",value=5,font=('Ink Free',12),fg="Red",bg="black",variable=myvar)
    btn.pack()
    btn.place(x=35,y=525)
    
    image = Image.open("images\Anightmare.jpg")
    resized= image.resize((180,220))
    test = ImageTk.PhotoImage(resized)
    img = Label(image=test)
    img.image = test
    img.place(x=215, y=300)
    btn=Radiobutton(vote,text="A Nightmare",value=6,font=('Ink Free',12),fg="Red",bg="black",variable=myvar)
    btn.pack()
    btn.place(x=225,y=525)
    
    image = Image.open("images\winchester.jpg")
    resized= image.resize((180,220))
    test = ImageTk.PhotoImage(resized)
    img = Label(image=test)
    img.image = test
    img.place(x=405, y=300)
    btn=Radiobutton(vote,text="Winchester",value=7,font=('Ink Free',12),fg="Red",bg="black",variable=myvar)
    btn.pack()
    btn.place(x=415,y=525)
    
    image = Image.open("images\Scream.jpg")
    resized= image.resize((180,220))
    test = ImageTk.PhotoImage(resized)
    img = Label(image=test)
    img.image = test
    img.place(x=595, y=300)
    btn=Radiobutton(vote,text="Scream",value=8,font=('Ink Free',12),fg="Red",bg="black",variable=myvar)
    btn.pack()
    btn.place(x=605,y=525)
    
    btn=Button(vote,text="Vote",command=Vote,fg="red",font=('Ink Free',15),bg="black",padx="20")
    btn.pack()
    btn.place(x=700,y=550)
    vote.configure(background='black')
    vote.mainloop()
    
root1 = tk.Tk()
root1.title("Login")
root1.geometry("800x600")
root1.resizable(False,False)
root1.configure(bg="black")
path = 'images/thenun.jpg'
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root1, image = img ,height=400,width=350)
panel.place(x=50,y=100)
numlable1= tk.Label(text="Login",fg='red',bg="black",font=('Comic Sans MS',32,'bold')).place(x=370,y=10)
numlable2= tk.Label(text="Username:",fg='red',bg="black",font=('Microsoft YaHei UI Light',14,'bold')).place(x=450,y=140)
numenter1=Entry(root1,width=40,font=('Microsoft YaHei UI Light',11))
numenter1.place(x=450,y=170)
numlable3= tk.Label(text="Password:",fg='red',bg="black",font=('Microsoft YaHei UI Light',14,'bold')).place(x=450,y=220)
numenter2=tk.Entry(root1,width=40,show="*",font=('Microsoft YaHei UI Light',11))
numenter2.place(x=450,y=250)
but1=tk.Button(text="Sign in",command=checkUser,bg='red',borderwidth=2, relief="raised",fg='black',border=0,height=2,width=42,cursor="hand2").place(x=466,y=310)
numlable4= tk.Label(text="Do not have an account?",font=('Microsoft YaHei UI Light',11),fg='red',bg="black").place(x=485,y=360)
but2=tk.Button(text="Sign Up",command=SignUp,bg='red',borderwidth=2, relief="raised",fg='black',border=0,height=2,width=42,cursor="hand2").place(x=466,y=400)
numlable5= tk.Label(text="",font=('Microsoft YaHei UI Light',11),fg='red',bg="white")
numlable5.place(x=466,y=450)
root1.mainloop()

clientSocket.close()