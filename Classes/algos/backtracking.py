from Classes.algos.performance import Performance
# from memory_profiler import memory_usage
import sys

class BackTracking(Performance):
    def __init__(self, n_queens, board, col) -> None:
        super().__init__()
        self.n_queens = n_queens
        self.board = board
        self.col = col
        self.board[0][col] = 1
        self.algorithm = 'BackTracking'
        self.number_of_rec = 0

    def is_safe(self, board, row, col):
        row_safe = self.row_check(board, row)
        col_safe = self.col_check(board, row, col)
        diagonal_safe = self.diagonal_check(board, row, col)
        return row_safe and col_safe and diagonal_safe

    def row_check(self, board, row):
        return not board[row].__contains__(1)

    def col_check(self, board, row, col):
        for c in range(col):
            if board[row][c] == 1:
                return False
        return True

    def diagonal_check(self, board, row, col):
        upper_right = True
        upper_left = True
        lower_right = True
        lower_left = True

        temp_row = row + 1
        temp_col = col + 1

        # check lower_right
        while temp_row < self.n_queens and temp_col < self.n_queens:
            if board[temp_row][temp_col] == 1:
                lower_right = False
                break
            temp_row += 1
            temp_col += 1

        # check lower_left
        temp_row = row + 1
        temp_col = col - 1
        while temp_row < self.n_queens and temp_col >= 0:
            if board[temp_row][temp_col] == 1:
                lower_left = False
                break
            temp_col -= 1
            temp_row += 1

        # check upper_right
        temp_row = row - 1
        temp_col = col + 1
        while temp_row >= 0 and temp_col < self.n_queens:
            if board[temp_row][temp_col] == 1:
                upper_right = False
                break
            temp_col += 1
            temp_row -= 1

        # check upper_left
        temp_row = row - 1
        temp_col = col - 1
        while temp_row >= 0 and temp_col >= 0:
            if board[temp_row][temp_col] == 1:
                upper_left = False
                break
            temp_col -= 1
            temp_row -= 1

        return upper_left and upper_right and lower_left and lower_right


    
    def backtrack_algo(self, col):
        
        print(col)
                    
        if col >= self.n_queens:

            # Capture memory usage at the end of each recursive call
            # self.memory_end = max(memory_usage())
            # print("end => ",self.memory_end)
            
            # Accumulate the memory usage for each recursive instance
            # self.memory += abs(self.memory_end - self.memory_start) / 1024
            # print(self.memory)

            return True
        
        if col == self.col and col < self.n_queens:
            col += 1
                    
           
        for row in range(self.n_queens):
            if self.is_safe(self.board, row, col):
                
                self.board[row][col] = 1
                self.number_of_rec += 1
                
                if self.backtrack_algo(col + 1):

                    self.unique += 1
                                        
                    return True
                
                self.board[row][col] = 0    
                
        return False
    
    
    def run(self):
        # self.pr.enable()
        self.start = self.timer()
        # Capture memory usage at the beginning of each recursive call
        # self.memory_start = memory_usage()[0]
        # print("start => ",self.memory_start)
        while not self.found_sol:
            self.backtrack_algo(0)
            
            if self.row_check(self.board, 1):
                self.board[0][self.col] = 0
                self.col = (self.col + 1) % (self.n_queens - 1)
                self.board[0][self.col] = 1
                self.number_of_tries += 1
            else:
                self.found_sol = True
                break
            
        function_size = self.func_size(self.backtrack_algo)
        print(function_size)
        self.memory = (self.number_of_rec * function_size) / 1024 
        print(self.number_of_rec)
        print(self.memory)
            
        self.end = self.timer()
        # self.pr.disable()
        self.execution_time()
        # self.pr.print_stats()
        
        
        
        
        
        
        
        
        
        
        
        
# n = 20

# board = [[0] * n for _ in range(n)]

# print(board)

# bt = BackTracking(n,board,2)
