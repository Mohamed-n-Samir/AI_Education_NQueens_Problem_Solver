from tkinter import *
from Classes.utils.configurationmenu import ConfigurationMenu

class App (ConfigurationMenu):

    def __init__(self) :

        super().__init__()
        
    def start(self):

        self.render_level_label()
        self.create_menubar()
        self.create_canvas()
        self.draw_board()
        self.render_queens()
        self.create_control_panel()
        self.window.protocol("WM_DELETE_WINDOW", self.destroy_all)
        self.window.mainloop()
        
    

App().start()