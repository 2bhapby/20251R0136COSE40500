import tkinter as tk
from add import add
from subtract import subtract
from multiply import multiply
from divide import divide


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Calculator")
        self.current_input = ""
        self.operator = None
        self.operand = None

        self.entry = tk.Entry(
            root, font=("Arial", 20), borderwidth=2, relief="solid", justify="right"
        )
        self.entry.grid(
            row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=10
        )

        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("+", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("-", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("*", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("C", 4, 2),
            ("/", 4, 3),
            ("=", 5, 0, 4),
        ]

        for text, row, col, colspan in [
            (*btn, 1) if len(btn) == 3 else btn for btn in buttons
        ]:
            tk.Button(
                root,
                text=text,
                width=9,
                height=2,
                font=("Arial", 14),
                command=lambda t=text: self.on_click(t),
            ).grid(row=row, column=col, columnspan=colspan, sticky="nsew")

    def on_click(self, char):
        if char in "0123456789.":
            self.current_input += char
            self.update_display(self.current_input)
        elif char in "+-*/":
            if self.current_input:
                self.operand = float(self.current_input)
                self.operator = char
                self.current_input = ""
        elif char == "=":
            if self.operator and self.current_input:
                try:
                    b = float(self.current_input)
                    if self.operator == "+":
                        result = add(self.operand, b)
                    elif self.operator == "-":
                        result = subtract(self.operand, b)
                    elif self.operator == "*":
                        result = multiply(self.operand, b)
                    elif self.operator == "/":
                        result = divide(self.operand, b)
                    else:
                        result = "Error"
                    self.update_display(str(result))
                    self.current_input = str(result)
                    self.operator = None
                except Exception:
                    self.update_display("Error")
                    self.current_input = ""
        elif char == "C":
            self.current_input = ""
            self.operator = None
            self.operand = None
            self.update_display("")

    def update_display(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, value)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
