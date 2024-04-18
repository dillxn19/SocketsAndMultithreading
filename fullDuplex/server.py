from tkinter import *
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 12345
s.bind((host,port))
root=Tk()
root.title("Server")

frame = Frame(root,bg = "black", width = 400, height = 400)
frame.pack()
entry = Entry(root, width = 65)
entry.pack()
button = Button(root, text = "Send", width = 55)
button.pack()

root.mainloop()