import math
import tkinter as tk
from maths_operations import factorial
from validate_entry import validate_entry

class Windows(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x300")
        self.title("Factorial de un número")

        self.widgets()

        self.mainloop()

    def widgets(self):
        self.label = tk.Label(self, text="Escribe el número")
        self.label.pack()

        vcmd = (self.register(validate_entry), '%P')
        self.entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.entry.pack()
        self.entry.focus_set()

        self.button = tk.Button(self, text="Calcular",
                                command=lambda: self.numberValidate())
        self.button.pack()

        self.factorial = tk.Label(self, text="Factorial: ")
        self.factorial.place(x=110, y=100)

        self.result_factorial = tk.Label(self, text="0")
        self.result_factorial.place(x=200, y=100)

        # events
        self.entry.bind("<Return>", lambda event: self.numberValidate())

    def numberValidate(self):
        number = self.entry.get()
        if number.isdigit():
            number = int(self.entry.get())
            result = math.factorial(number)
            self.result_factorial.config(text=result)
        else:
            self.result_factorial.config(text="0")
            print("el número no es correcto")
