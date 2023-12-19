from tkinter import Frame, Label, CENTER,Toplevel
from Classes.utils.chessboard import NCanvas
from Classes.utils.comparewindow import CompareWindow
from Classes.utils.nbutton import NButton
import threading
from matplotlib import pyplot as plt


# Controller of the game
class ControlPanel(NCanvas):
    def __init__(self):
        super().__init__()
        self.compare_windows = []

    def create_control_panel(self):
        btn_frame = Frame(self.control_frame, width=self.board_size, padx=50)

        btn_frame.grid(row=0, column=0, sticky="nsew")

        self.backtrack_solve_button = NButton(
            btn_frame, "BackTracking", "#4CAF50", callback=self.backtrack
        )
        
        self.bestfirst_solve_button = NButton(
            btn_frame, "BestFirst", "#4CAF50", callback=self.bestfirst
        )
        
        self.hillclimbing_solve_button = NButton(
            btn_frame, "HillClimbing", "#4CAF50", callback=self.hillclimb
        )
        
        self.genetic_solve_button = NButton(
            btn_frame, "Genetic", "#4CAF50", callback=self.genetic
        )
        
        self.selected_algos_solve = NButton(
            btn_frame, "Compare", "#f4a41a", callback=self.run_selected_algos
        )
        
        NButton(btn_frame, "Reset", "#FF5733", callback=self.reset_game)

    def backtrack(self):
        self.backtrack_solve_button.btn.config(background="#eeeeee")
        self.backtrack_solve_button.btn.config(state="disabled")
        self.bestfirst_solve_button.btn.config(background="#eeeeee")
        self.bestfirst_solve_button.btn.config(state="disabled")
        self.hillclimbing_solve_button.btn.config(background='#eeeeee')
        self.hillclimbing_solve_button.btn.config(state="disabled")
        self.genetic_solve_button.btn.config(background='#eeeeee')
        self.genetic_solve_button.btn.config(state="disabled")
        self.selected_algos_solve.btn.config(background='#eeeeee')
        self.selected_algos_solve.btn.config(state="disabled")
        self.backtrack_solve()
        
    def bestfirst(self):
        self.backtrack_solve_button.btn.config(background="#eeeeee")
        self.backtrack_solve_button.btn.config(state="disabled")
        self.bestfirst_solve_button.btn.config(background="#eeeeee")
        self.bestfirst_solve_button.btn.config(state="disabled")
        self.hillclimbing_solve_button.btn.config(background='#eeeeee')
        self.hillclimbing_solve_button.btn.config(state="disabled")
        self.genetic_solve_button.btn.config(background='#eeeeee')
        self.genetic_solve_button.btn.config(state="disabled")
        self.selected_algos_solve.btn.config(background='#eeeeee')
        self.selected_algos_solve.btn.config(state="disabled")
        self.bestfirst_solve()
        
    def hillclimb(self):
        self.backtrack_solve_button.btn.config(background="#eeeeee")
        self.backtrack_solve_button.btn.config(state="disabled")
        self.bestfirst_solve_button.btn.config(background="#eeeeee")
        self.bestfirst_solve_button.btn.config(state="disabled")
        self.hillclimbing_solve_button.btn.config(background='#eeeeee')
        self.hillclimbing_solve_button.btn.config(state="disabled")
        self.genetic_solve_button.btn.config(background='#eeeeee')
        self.genetic_solve_button.btn.config(state="disabled")
        self.selected_algos_solve.btn.config(background='#eeeeee')
        self.selected_algos_solve.btn.config(state="disabled")
        self.hillclimbing_solve()
        
    def genetic(self):
        self.backtrack_solve_button.btn.config(background="#eeeeee")
        self.backtrack_solve_button.btn.config(state="disabled")
        self.bestfirst_solve_button.btn.config(background="#eeeeee")
        self.bestfirst_solve_button.btn.config(state="disabled")
        self.hillclimbing_solve_button.btn.config(background='#eeeeee')
        self.hillclimbing_solve_button.btn.config(state="disabled")
        self.genetic_solve_button.btn.config(background='#eeeeee')
        self.genetic_solve_button.btn.config(state="disabled")
        self.selected_algos_solve.btn.config(background='#eeeeee')
        self.selected_algos_solve.btn.config(state="disabled")
        self.genetic_solve()
        
    def find_best_performance(self,data_array):
        if not data_array:
            return "No data provided"

        # Initialize with the first element
        best_time = data_array[0]
        best_memory = data_array[0]
        best_tries = data_array[0]

        for entry in data_array[1:]:
            # Compare execution time
            if float(entry['Execution time'][:-7]) < float(best_time['Execution time'][:-7]):
                best_time = entry

            # Compare memory consumption
            if float(entry['Memory Consumed'][:-3]) < float(best_memory['Memory Consumed'][:-3]):
                best_memory = entry

            # Compare number of tries
            if int(entry['Number Of Tries'].split()[0]) < int(best_tries['Number Of Tries'].split()[0]):
                best_tries = entry
                
        # Create a Toplevel window
        result_window = Toplevel(self.window)

        # Add labels with the information to the Toplevel window
        Label(result_window, text=f"Best Time: {best_time['Algorithm']}",pady=10,font=("Arial",16)).pack()
        Label(result_window, text=f"Best Memory: {best_memory['Algorithm']}",pady=10,font=("Arial",16)).pack()
        Label(result_window, text=f"Best Tries: {best_tries['Algorithm']}",pady=10,font=("Arial",16)).pack()
        
        result_window.geometry("400x300")
        result_window.update_idletasks()
        result_window.grab_set()


        return f"Best Time: {best_time['Algorithm']}, Best Memory: {best_memory['Algorithm']}, Best Tries: {best_tries['Algorithm']}"

        
    def run_selected_algos(self):
        self.selected_algos_solve.btn.config(background='#eeeeee')
        self.selected_algos_solve.btn.config(state="disabled")
        dicts = []
        for algo in self.algos:
            title = "BackTracking" if algo == 0 else ("BestFirst" if algo == 1 else ("HillClimbing" if algo == 2 else "Genatic"))     
            print(algo)
            cw = CompareWindow(root=self.window,title=title,number_of_queens=self.number_of_queens,algo=algo)
            self.compare_windows.append(cw)
            dicts.append(cw.data_dict)
            
        print(self.find_best_performance(dicts))
            

    
    # def run_selected_algos(self):
    #     threads = []

    #     for algo in self.algos:
    #         title = "BackTracking" if algo == 0 else ("BestFirst" if algo == 1 else ("HillClimbing" if algo == 2 else "Genetic"))
    #         print(algo)
    #         cw = CompareWindow(root=self.window, title=title, number_of_queens=self.number_of_queens, algo=algo)

    #         # Create a thread for each CompareWindow
    #         thread = threading.Thread(target=lambda: cw.switch_case(algo))
    #         threads.append(thread)

    #     # Start all threads
    #     for thread in threads:
    #         thread.start()

    #     # Wait for all threads to finish
    #     # for thread in threads:
    #     #     thread.join()
        
    def reset_game(self):
        self.reset_board()
        self.backtrack_solve_button.btn.config(background="#4CAF50")
        self.backtrack_solve_button.btn.config(state="normal")
        self.bestfirst_solve_button.btn.config(background="#4CAF50")
        self.bestfirst_solve_button.btn.config(state="normal")
        self.hillclimbing_solve_button.btn.config(background='#4CAF50')
        self.hillclimbing_solve_button.btn.config(state="normal")
        self.genetic_solve_button.btn.config(background='#4CAF50')
        self.genetic_solve_button.btn.config(state="normal")
        self.selected_algos_solve.btn.config(background='#f4a41a')
        self.selected_algos_solve.btn.config(state="normal")
        plt.close('all')
        for window in self.compare_windows:
            window.destroy_self()
            
