# client.py
import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

HOST = "127.0.0.1"
PORT = 5555

class ChatClient:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tkinter Chat App")

        self.chat_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD)
        self.chat_area.pack(padx=10, pady=10)
        self.chat_area.config(state=tk.DISABLED)

        self.msg_entry = tk.Entry(self.window)
        self.msg_entry.pack(fill=tk.X, padx=10, pady=5)
        self.msg_entry.bind("<Return>", self.send_message)

        self.send_btn = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_btn.pack(pady=5)

        self.nickname = simpledialog.askstring("Nickname", "Enter your nickname", parent=self.window)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.window.mainloop()

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode("utf-8")
                if message == "NICK":
                    self.client.send(self.nickname.encode("utf-8"))
                else:
                    self.chat_area.config(state=tk.NORMAL)
                    self.chat_area.insert(tk.END, message + "\n")
                    self.chat_area.config(state=tk.DISABLED)
                    self.chat_area.yview(tk.END)
            except:
                break

    def send_message(self, event=None):
        message = f"{self.nickname}: {self.msg_entry.get()}"
        self.client.send(message.encode("utf-8"))
        self.msg_entry.delete(0, tk.END)

    def close(self):
        self.client.close()
        self.window.destroy()

ChatClient()
