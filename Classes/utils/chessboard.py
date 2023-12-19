from tkinter import Canvas, CENTER, CURRENT
from Classes.utils.queens import Queens
from Classes.algos.backtracking import BackTracking
from Classes.algos.hillclimbing import HellClimbing
from Classes.algos.genetic import Genetic
from Classes.algos.bestfirst import BFS
import random,gc



# Main class for chess board playground
class NCanvas(Queens):
    def __init__(self):
        super().__init__()
        self.__size = self.board_size
        self.__parent = self.play_frame
        self.board = []

    def create_canvas(self):
        self.board = []
        canvas = Canvas(
            self.__parent, width=self.__size, height=self.__size, bg="white"
        )
        canvas.grid(row=1, column=0)
        self.canvas = canvas
        for i in range(0, self.queens.get()):
            row = []
            for k in range(0, self.queens.get()):
                row.append(0)
            self.board.append(row)

    def draw_board(self):
        queens = self.queens.get()
        box_size = self.__size / queens
        for row in range(0, queens):
            for col in range(0, queens):
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
        self.render_queens()

    def add_queen(self, row, col):
        queens = self.queens.get()
        box_size = self.__size / queens

        x = row * (box_size) + (int(box_size / 2))
        y = col * (box_size) + (int(box_size / 2))

        queenid = self.canvas.create_image(
            x, y, image=self.queen_img, anchor=CENTER, tags=(row, col)
        )
        self.canvas.tag_bind(queenid, "<Button-3>", lambda: None)
        self.board[row][col] = 1

        self.pop_queens()

    def remove_queen(self, row, col):
        self.canvas.delete(((row + col) + 1))
        self.board[row][col] = 0
        self.append_queens()

    # Generate randon n Queens

    def random_col(self):
        return random.choice(range(self.queens.get()))

    # Draw board after solu.

    def draw_solved_board(self,data_dict = {}):
        rectId = 1
        for row in range(self.queens.get()):
            for col in range(self.queens.get()):
                if self.board[row][col] == 1:
                    self.add_queen(row, col)
                    self.canvas.itemconfig((rectId,), outline="#4FBF26", width=5)
                rectId += 1
        if self.number_of_queens == self.queens.get() - 1:
            self.lose_handler(self.queens.get())
            return
        else: 
            if self.number_of_queens == 0:
                self.success_handler(data_dict)
                return

    # Functions to generate the solution
    
    # BackTracking
    def backtrack_solve(self):
        bt = BackTracking(self.queens.get(), self.board, self.random_col())
        bt.run()
        if bt.found_sol :
            data_dict = {'Algorithm':f'{bt.algorithm}','NumberOfQueens':f'{self.queens.get()}','Execution time': f'{bt.time_in_sec:.4f} Seconds', "Memory Consumed": f'{bt.memory} KBs','Number Of Tries': f'{bt.number_of_tries} Try', 'Deepest Level': f'{bt.unique}' }
            self.draw_solved_board(data_dict)
        
    # BestFirstSearch
    def bestfirst_solve(self):
        bfs = BFS(self.queens.get(),self.board)
        bfs.run()
        data_dict = {'Algorithm':f'{bfs.algorithm}','NumberOfQueens':f'{self.queens.get()}','Execution time': f'{bfs.time_in_sec:.4f} Seconds', "Memory Consumed": f'{bfs.memory} KBs','Number Of Tries': f'{bfs.number_of_tries} Try', 'Boards Generated': f'{bfs.unique}' }
        self.draw_solved_board(data_dict)
        
    # HillClimbing    
    def hillclimbing_solve(self):
        hc = HellClimbing(self.queens.get(),self.board)
        hc.run()
        if hc.final_sol != None:
            data_dict = {'Algorithm':f'{hc.algorithm}','NumberOfQueens':f'{self.queens.get()}','Execution time': f'{hc.time_in_sec:.4f} Seconds', "Memory Consumed": f'{hc.memory} KBs','Number Of Tries': f'{hc.number_of_tries} Try', 'Generated neighbors': f'{hc.unique}' }
            self.draw_solved_board(data_dict)
    
    # Genetic
    def genetic_solve(self):
        gen = Genetic(self.queens.get(),self.board)
        sol = gen.run()
        if sol != None:
            data_dict = {'Algorithm':f'{gen.algorithm}','NumberOfQueens':f'{self.queens.get()}','Execution time': f'{gen.time_in_sec:.4f} Seconds', "Memory Consumed": f'{gen.memory} KBs','Number Of Tries': f'{gen.number_of_tries} Try', 'Number Of Generation': f'{gen.unique}' }
            self.draw_solved_board(data_dict)
