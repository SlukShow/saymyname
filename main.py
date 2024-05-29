import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog

def choose_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        label.config(text="Вибраний файл: " + file_path)

def button_command():
    label.config(text="В'ячеслав")

if __name__ == "__main__":
    root = tk.Tk()

    root.title("Say My Name")
    # setting window size
    width = 300
    height = 150
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    label = tk.Label(root)
    ft = tkFont.Font(family='Times', size=10)
    label["font"] = ft
    label["fg"] = "#333333"
    label["justify"] = "center"
    label["text"] = ""
    label.place(x=25, y=10, width=258, height=30)

    button_say_name = tk.Button(root)
    button_say_name["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times', size=10)
    button_say_name["font"] = ft
    button_say_name["fg"] = "#000000"
    button_say_name["justify"] = "center"
    button_say_name["text"] = "Say My Name"
    button_say_name["command"] = button_command
    button_say_name.place(x=10, y=50, width=280, height=30)

    button_choose_file = tk.Button(root)
    button_choose_file["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times', size=10)
    button_choose_file["font"] = ft
    button_choose_file["fg"] = "#000000"
    button_choose_file["justify"] = "center"
    button_choose_file["text"] = "Обрати файл"
    button_choose_file["command"] = choose_file
    button_choose_file.place(x=10, y=100, width=280, height=30)

    root.mainloop()
