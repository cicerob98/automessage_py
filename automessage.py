import pyautogui
from time import sleep
import keyboard
import os
import threading
from tkinter import *

def keyListener():
    while True:
        if keyboard.is_pressed('esc'): # it will stop working by clicking 'esc' you can change to to any key
            os._exit(0)

def typing():
    sleep(5)
    message = message_entry.get()
    try:
        total_messages = int(text_entry.get())
    except ValueError:
        raise Exception("Digite um número inteiro.")

    while total_messages > 0:

        pyautogui.write(message, interval= 0.2) # it will write the typed message with interval to simulate a user typing
        pyautogui.press('enter')
        total_messages -= 1

        sleep(3)

interface = Tk()

interface.minsize(323, 220) # set min width and height
interface.maxsize(323, 220) # set max width and height

interface.title("Auto Message")
message_quest = Label(interface, text="Digite qual mensagem deseja enviar.")
message_quest.grid(column=0, row=0, padx=10, pady=10)

message_entry = Entry(interface, width = 50)
message_entry.grid(column=0, row=1, padx=10, pady=10)
message_entry.focus_set()


text = Label(interface, text="Digite a quantidade de mensagens que deseja enviar.")
text.grid(column=0, row=2, padx=10, pady=10)

text_entry = Entry(interface, width = 20)
text_entry.grid(column=0, row=3, padx=10, pady=10)

bt = Button(interface, text="Escrever Mensagens", command=typing)
bt.grid(column=0, row=4, padx=10, pady=10)

threading.Thread(target=keyListener).start()
threading.Thread(interface.mainloop())