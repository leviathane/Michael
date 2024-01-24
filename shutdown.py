import tkinter as tk
from tkinter import simpledialog
import os
import time

def shutdown():
    while True:
        try:
            minutes = simpledialog.askinteger("Shutdown Timer", "Enter the number of minutes to shutdown:")
            if minutes is not None:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if minutes is not None:
        shutdown_message.config(text=f"Computer will shutdown in {minutes} minutes")
        time.sleep(minutes * 60)
        os.system("shutdown /s /t 1")
        shutdown_message.config(text="Computer has been shutdown")
root = tk.Tk()
root.title("Shutdown Timer")
shutdown_button = tk.Button(root, text="Shutdown", command=shutdown)
shutdown_button.pack(pady=10)
shutdown_message = tk.Label(root, text="")
shutdown_message.pack()

