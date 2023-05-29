import pyautogui
from time import sleep
import keyboard
from tkinter import *


def typing():
    sleep(5)
    global entry
    string = entry.get()
    while True:
        pyautogui.write(string, interval= 0.1)
        pyautogui.press('enter')
        if keyboard.is_pressed('esc'):
            break

interface = Tk()

interface.title("Auto Message")
text = Label(interface, text="Digite qual mensagen deseja enviar e clique no botão abaixo para iniciar.")
text.grid(column=0, row=0, padx=10, pady=10)

entry = Entry(interface, width= 50)
entry.grid(column=0, row=1, padx=10, pady=10)
entry.focus_set()

bt = Button(interface, text="Escrever Mensagens", command=typing)
bt.grid(column=0, row=2, padx=10, pady=10)

interface.mainloop()


# if __name__ == "__main__":
#     typing()
#-------------------------------------------------------#
# pyautogui.click(601, 998) auto click na coordenada