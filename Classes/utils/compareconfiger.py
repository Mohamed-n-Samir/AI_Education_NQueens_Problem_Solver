from tkinter import IntVar, Toplevel, Label, Entry, TclError,Checkbutton, Button
from tkinter.messagebox import showwarning
from Classes.utils.controlpanel import ControlPanel
from Classes.utils.levellabel import Level_Label
from Classes.utils.nbutton import NButton



class CompareConfiger(ControlPanel):
    def __init__(self):
        ControlPanel.__init__(self)
        self.selected_boxes = [IntVar() for _ in range(4)]  # List to store the checkbox states

    def create_compare_config_box(self):
        compare_window = Toplevel(self.window)
        self.__compare_window = compare_window
        compare_window.geometry("300x200")
        compare_window.title("Comparison Settings")

        self.checkboxes = []

        checkbox1 = Checkbutton(compare_window, text="BackTracking", variable=self.selected_boxes[0])
        checkbox1.pack(padx=10, pady=5)
        self.checkboxes.append(checkbox1)
        checkbox2 = Checkbutton(compare_window, text="BestFirst", variable=self.selected_boxes[1])
        checkbox2.pack(padx=10, pady=5)
        self.checkboxes.append(checkbox2)
        checkbox3 = Checkbutton(compare_window, text="HillClimbing", variable=self.selected_boxes[2])
        checkbox3.pack(padx=10, pady=5)
        self.checkboxes.append(checkbox3)
        checkbox4 = Checkbutton(compare_window, text="Genetic", variable=self.selected_boxes[3])
        checkbox4.pack(padx=10, pady=5)
        self.checkboxes.append(checkbox4)

        save_button = Button(compare_window, text="Save",background="#4287f5", command=self.save_selections,width=30,height=20)
        save_button.pack(pady=10)

    def save_selections(self):
        selected_indices = [i for i, var in enumerate(self.selected_boxes) if var.get() == 1]
        print("Selected boxes:", selected_indices)  # Print selected checkbox indices
        self.algos = [*selected_indices]
        self.__compare_window.destroy()

# Usage:
# Assuming ControlPanel is a base class with `window` initialized, similar to your existing code.
# Instantiate CompareConfiger and create the compare configuration box.
# compare_config = CompareConfiger()
# compare_config.create_compare_config_box()