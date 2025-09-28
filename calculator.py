import tkinter as tk

from unicodedata import digit

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE =("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class calculator:
    def create_display_frame(self):
        frame = tk.Frame(self.window, height = 221, bg = LIGHT_GRAY)
        frame.pack(expand = True, fill = 'both')
        return frame
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand = True, fill = 'both')
        return frame
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text = self.total_expression, anchor = tk.E, bg = LIGHT_GRAY, fg = LABEL_COLOR, padx = 24, font = SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')
        label = tk.Label(self.display_frame, text=self.current_expression, anchor = tk.E, bg = LIGHT_GRAY, fg = LABEL_COLOR, padx = 24, font = LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')
        return total_label, label
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title('aniket calc')
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_display_frame()
        self.total_expression = "0"
        self.current_expression = "0"
        self.total_label, self.label = self.create_display_labels()
        self.digits = {7:(1,1), 8:(1,2), 9:(1,3), 4:(2,1), 5:(2,2), 6:(2,3), 1:(3,1), 2:(3,2), 3:(3,3)}
        self.operations = {"/":"\u00F7", "*":"\u00D7", "-":"-", "+":"+"}
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

    def run(self):
        self.window.mainloop()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky= tk.NSEW)
            i += 1

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, columnspan=2, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()

    def update_total_label_label(self):
        self.label.configtext(text = self.current_expression)

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_label += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        self.total_expression = str(eval(self.total_expression))
        self.total_expression = ""
        self.update_label()




if __name__ == "__main__":
    calc = calculator()
    calc.run()

