from tkinter import *
import socket, threading
root=Tk()
root.title("Client")

def send_data():
    a = entry.get()
    entry.delete(0,END)
    new_label = Label(frame, text = a, fg = "green", anchor = "e")
    new_label.pack(side = TOP)
    s.sendall(a.encode())

def get_data():
    while True:
        data = s.recv(1024).decode("utf-8")
        print(data)
        chat = Label(frame, text = data, fg = "red", anchor = "w")
        chat.pack(side = TOP)

host = 'localhost'
port = 24680
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
recp = threading.Thread(target = get_data)
recp.start()

frame = Frame(root,bg = "black", width = 400, height = 400)
frame.pack()
entry = Entry(root, width = 65)
entry.pack()
button = Button(root, text = "Send", width = 55, command = send_data)
button.pack()



root.mainloop()