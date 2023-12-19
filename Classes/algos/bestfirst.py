from queue import PriorityQueue
from Classes.algos.performance import Performance
from matplotlib import pyplot as plt


class BFS(Performance):
    
    def __init__(self,number_of_queens,board) -> None:
        super().__init__()
        self.number_of_queens = number_of_queens
        self.board = board
        self.algorithm = 'BestFirst'
        self.size = 0
        self.elapsed_times = []
        self.heuristic_values = []
        

    def is_valid(self,board, row, col):
        for prev_row in range(row):
            if (
                board[prev_row] == col
                or board[prev_row] - prev_row == col - row
                or board[prev_row] + prev_row == col + row
            ):
                return False
        return True


    def assign_board(self,board):
        for row in range(len(board)):
            for col in range(len(board)):
                self.board[row][col] = 1 if board[row] == col else 0


    def calculate_heuristic(self,board):
        conflicts = 0
        for i in range(len(board)):
            for j in range(i + 1, len(board)):
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1
        return conflicts


    def bfs(self):
        queue = PriorityQueue()
        queue.put((self.calculate_heuristic([]), []))
        while not queue.empty():
            _, board = queue.get()
            row = len(board)

            if row == self.number_of_queens:
                self.assign_board(board)
                return

            for col in range(self.number_of_queens):
                
                if self.is_valid(board, row, col):
                    new_board = board + [col]
                    self.size += self.func_size(new_board)
                    heuristic = self.calculate_heuristic(new_board)
                    print(heuristic)
                    queue.put((heuristic, new_board))
                    self.heuristic_values.append(heuristic)
                    elapsed_time = self.timer() - self.start
                    self.elapsed_times.append(elapsed_time)
                    self.unique += 1
        
    def run(self):
        self.start = self.timer()
        
        self.bfs()
        function_size = self.func_size(self.bfs)
        # print(function_size)
        self.memory = (self.size + function_size) / 1024 
        print(self.unique)
        print(self.memory)
            
        self.end = self.timer()
        # self.pr.disable()
        self.execution_time()
        self.plot_hero()
        
    def plot_hero(self):
        # Plotting
        plt.figure(figsize=(10, 5))
        plt.plot(self.elapsed_times,self. heuristic_values, marker='o', linestyle='-', color='b')
        plt.title('BFS Heuristic Values over Time')
        plt.xlabel('Elapsed Time (seconds)')
        plt.ylabel('Heuristic Value')
        plt.grid(True)
        plt.show(block=False)

# n = 15
# board = [[0] * n for _ in range(n)]
# bfs = BFS(n,board)
# bfs.bfs_solu()
