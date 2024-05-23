from tkinter import *
import socket, threading

def send_data():
    a = entry.get()
    entry.delete(0,END)
    new_label = Label(frame, text = a, fg = "green", borderwidth=2, relief="solid")
    new_label.pack(anchor = "e", columnspan = 1)
    conn.sendall(a.encode())

# def on_return():
#     print("key pressed")

def get_data():
    while True:
        data = conn.recv(1024).decode("utf-8")
        print(data)
        chat = Label(frame, text = data, fg = "red", anchor = "w")
        chat.pack(side = TOP)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 24680
s.bind((host,port))
s.listen(5)
conn, addr = s.accept()
recp = threading.Thread(target = get_data)
recp.start()


root=Tk()
root.title("Server")


frame = Frame(root,bg = "black", width = 400, height = 400)
frame.pack()
entry = Entry(root, width = 65)
entry.pack()
# entry.bind(("<Return>", on_return))
button = Button(root, text = "Send", width = 55, command = send_data)
button.pack()



root.mainloop()