import tkinter as tk
from tkinter import messagebox
from calculator import Calculator

class CalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Calculator")
        self.geometry("320x420")
        self.resizable(False, False)
        self.calc = Calculator()
        self._build_ui()

    def _build_ui(self):
        self.display_var = tk.StringVar(value="")
        display = tk.Entry(self, textvariable=self.display_var, font=("Arial", 20),
                           bd=5, relief=tk.RIDGE, justify="right")
        display.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)

        btns = [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            ["0",".","=","+"],
            ["C","±","x^y","%"]
        ]

        for row in btns:
            frame = tk.Frame(self)
            frame.pack(expand=True, fill="both")
            for label in row:
                b = tk.Button(frame, text=label, font=("Arial",16), bd=1,
                              command=lambda l=label: self.on_button(l))
                b.pack(side=tk.LEFT, expand=True, fill="both", padx=2, pady=2)

    def on_button(self, label):
        if label == "C":
            self.display_var.set("")
            return
        if label == "±":
            txt = self.display_var.get()
            try: self.display_var.set(str(-float(txt)))
            except: messagebox.showerror("Error","Invalid number")
            return
        if label == "=":
            expr = self.display_var.get().replace("%", "/100*")
            try: self.display_var.set(str(eval(expr, {"__builtins__":None}, {})))
            except Exception as e: messagebox.showerror("Error", e)
            return
        if label == "x^y": self.display_var.set(self.display_var.get()+"**")
        else: self.display_var.set(self.display_var.get()+label)

if __name__ == "__main__":
    app = CalculatorGUI()
    app.mainloop()
