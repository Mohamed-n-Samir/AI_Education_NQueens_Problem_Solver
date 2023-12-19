from tkinter import Menu,Label,PhotoImage
from tkinter.messagebox import askyesno
from Classes.utils.levelconfiger import LevelConfiger
from Classes.utils.compareconfiger import CompareConfiger



# Setting MenuBar
class ConfigurationMenu(LevelConfiger,CompareConfiger):
    
    def __init__(self):
        LevelConfiger.__init__(self)
        CompareConfiger.__init__(self)


    def create_menubar(self):
        menubar = Menu(self.window)
        filemenu = Menu(menubar, tearoff=False)
        filemenu.add_command(label="Level", command=self.create_level_config_box,font=('Arial',14))
        filemenu.add_command(label="compare", command=self.create_compare_config_box,font=('Arial',14))
        filemenu.add_command(label="Quit", command=self.exit,font=('Arial',14))

        menubar.add_cascade(label="Settings", menu=filemenu,font=('Arial',16),image=self.setting_img)
        self.window.config(menu=menubar)

    def exit(self):
        if askyesno("Quit", "Are you sure you want to Quit?"):
            exit(1)
        else:
            return
