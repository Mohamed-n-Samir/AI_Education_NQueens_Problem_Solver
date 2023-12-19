from tkinter import Tk, Toplevel,IntVar,Frame,PhotoImage,Canvas,CENTER, CURRENT
from Classes.utils.gamesuccesshandler import GameSuccessHandler
from Classes.utils.gamelosehandler import GameLoseHandler
from Classes.algos.backtracking import BackTracking
from Classes.algos.bestfirst import BFS 
from Classes.algos.hillclimbing import HellClimbing
from Classes.algos.genetic import Genetic
import random,time

class Board(object):
    def __init__(self,root,title,number_of_queens):
        self.board_size = 600
        self.window = Toplevel(root)
        self.window.configure(borderwidth=0,highlightthickness=0,padx=0,pady=0)
        self.window.resizable(False, False)
        self.window.title(title)
        self.queens = IntVar()
        self.queens.set(number_of_queens)

        self.queen_img = PhotoImage(file="Images/queen.png")

        self.body_frame = Frame(self.window,padx=0,pady=0)
        self.body_frame.pack()

        self.play_frame = Frame(self.body_frame,padx=0,pady=0)
        self.play_frame.pack()


class Queens(Board):
    def __init__(self,root,title,number_of_queens):
        if not hasattr(self, "window"):
            super().__init__(root,title,number_of_queens)

        self.col = 0
        self.success_handler = GameSuccessHandler(root).handler
        self.lose_handler = GameLoseHandler(root).handler
        self.number_of_queens = self.queens.get()


    def pop_queens(self):
        if self.number_of_queens == 0:
            return

        self.number_of_queens -= 1




class NCanvas(Queens):
    def __init__(self,root,title,number_of_queens):
        super().__init__(root,title,number_of_queens)
        self.__size = self.board_size
        self.__parent = self.play_frame
        self.board = []
        self.nqueens = self.queens.get()

    def create_canvas(self):
        self.board = []
        self.canvas = Canvas(
            self.__parent, width=self.__size, height=self.__size, bg="white"
        )
        self.canvas.grid(row=0, column=0)
        # self.canvas = canvas
        for i in range(0, self.nqueens):
            row = []
            for k in range(0, self.nqueens):
                row.append(0)
            self.board.append(row)

    def draw_board(self):
        box_size = self.__size / self.nqueens
        for row in range(0, self.nqueens):
            for col in range(0, self.nqueens):
                x1, y1 = row * box_size, col * box_size
                x2, y2 = x1 + box_size, y1 + box_size
                color = "white"
                if (row + col) % 2 != 0:
                    color = "#3b3a37"

                self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=color, tags=f"{row},{col}", outline="gray"
                )

    def reset_board(self):
        self.create_canvas()
        self.draw_board()

    def add_queen(self, row, col):
        queens = self.queens.get()
        box_size = self.__size / queens

        x = row * (box_size) + (int(box_size / 2))
        y = col * (box_size) + (int(box_size / 2))

        queenid = self.canvas.create_image(
            x, y, image=self.queen_img, anchor=CENTER, tags=(row, col)
        )
        self.canvas.tag_bind(queenid, "<Button-3>", lambda: self.canvas.create_image(
            x, y, image=self.queen_img, anchor=CENTER, tags=(row, col)
        ))

        self.pop_queens()

    # Generate randon n Queens

    def random_col(self):
        return random.choice(range(self.nqueens))

    # Draw board after solu.

    def draw_solved_board(self,data_dict = {}):
        rectId = 1
        for row in range(self.nqueens):
            for col in range(self.nqueens):
                if self.board[row][col] == 1:
                    self.add_queen(row, col)
                    self.canvas.itemconfig((rectId,), outline="#4FBF26", width=5)
                rectId += 1
        if self.number_of_queens == self.nqueens - 1:
            self.lose_handler(self.nqueens)
            return
        else: 
            if self.number_of_queens == 0:
                self.success_handler(data_dict)
                return


class CompareWindow(NCanvas):
    def __init__(self, root,title,number_of_queens,algo):
        super().__init__(root,title,number_of_queens)
        self.comp_window = self.window
        self.comp_window.geometry("600x600")
        self.comp_window.title(title)

        self.__size = 300  # Modify size as needed
        self.__parent = self.comp_window

        self.data_dict = {}
        self.create_canvas()
        self.draw_board()
        time.sleep(0.00001)
        self.switch_case(algo)
        self.draw_solved_board(self.data_dict)
        


    def switch_case(self,case_number):
        if case_number == 0:
            bt=  BackTracking(self.queens.get(), self.board, self.random_col())
            bt.run()
            self.data_dict = {'Algorithm':f'{bt.algorithm}','NumberOfQueens':f'{self.queens.get()}','Execution time': f'{bt.time_in_sec:.4f} Seconds', "Memory Consumed": f'{bt.memory} KBs','Number Of Tries': f'{bt.number_of_tries} Try', 'Deepest Level': f'{bt.unique}' }.copy()
        elif case_number == 1:
            bfs =  BFS(self.queens.get(),self.board)
            bfs.run()
            self.data_dict = {'Algorithm':f'{bfs.algorithm}','NumberOfQueens':f'{self.queens.get()}','Execution time': f'{bfs.time_in_sec:.4f} Seconds', "Memory Consumed": f'{bfs.memory} KBs','Number Of Tries': f'{bfs.number_of_tries} Try', 'Boards Generated': f'{bfs.unique}' }.copy()
        elif case_number == 2:
            hc = HellClimbing(self.queens.get(),self.board)
            hc.run()
            self.data_dict = {'Algorithm':f'{hc.algorithm}','NumberOfQueens':f'{self.queens.get()}','Execution time': f'{hc.time_in_sec:.4f} Seconds', "Memory Consumed": f'{hc.memory} KBs','Number Of Tries': f'{hc.number_of_tries} Try', 'Generated neighbors': f'{hc.unique}' }.copy()
        elif case_number == 3:
            gen =  Genetic(self.queens.get(),self.board)
            gen.run()
            self.data_dict = {'Algorithm':f'{gen.algorithm}','NumberOfQueens':f'{self.queens.get()}','Execution time': f'{gen.time_in_sec:.4f} Seconds', "Memory Consumed": f'{gen.memory} KBs','Number Of Tries': f'{gen.number_of_tries} Try', 'Total Number Of Generation': f'{gen.unique}' }.copy()
    
    def destroy_self(self):
        self.window.destroy()


        


        
