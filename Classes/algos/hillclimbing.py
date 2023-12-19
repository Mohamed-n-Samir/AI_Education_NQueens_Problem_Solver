from random import randint, shuffle
from Classes.algos.performance import Performance
import matplotlib.pyplot as plt

class HellClimbing(Performance):

    def __init__(self, number_of_queens,board) -> None:
        super().__init__()
        self.number_of_queens = number_of_queens
        self.state = [i for i in range(number_of_queens)]
        self.board = board
        self.final_sol = None
        self.configure_randomly()
        self.algorithm = "HillClimbing"
        self.size = 0
        self.heuristic_values = []
        self.elapsed_times = []
        

    # A Random Start
    def configure_randomly(self):
        shuffle(self.state)
        for i in range(self.number_of_queens):
            self.board[self.state[i]][i] = 1


    # Print Board
    def print_board(self):
        for i in range(self.number_of_queens):
            print(*self.board[i])


    # Compare States
    def compare_states(self,state1, state2):
        for i in range(self.number_of_queens):
            if state1[i] != state2[i]:
                return False

        return True


    # Reset given board
    def board_reset(self,board):
        board[:] = [[0] * self.number_of_queens for _ in range(self.number_of_queens)]


    # Find heuristic
    def find_heuristic(self,board, state):
        attacking = 0

        for i in range(self.number_of_queens):
            # Check Row
            row = state[i]
            state_count = board[row].count(1)
            if state_count > 1:
                attacking += state_count - 1

            # Check left up Diagonal
            row = state[i] - 1
            col = i - 1
            while col >= 0 and row >= 0 and board[row][col] != 1:
                col -= 1
                row -= 1

            if col >= 0 and row >= 0 and board[row][col] == 1:
                attacking += 1

            # Check right down Diagonal
            row = state[i] + 1
            col = i + 1
            while (
                col < self.number_of_queens and row < self.number_of_queens and board[row][col] != 1
            ):
                col += 1
                row += 1

            if col < self.number_of_queens and row < self.number_of_queens and board[row][col] == 1:
                attacking += 1

            # Check left down Diagonal
            row = state[i] + 1
            col = i - 1
            while col >= 0 and row < self.number_of_queens and board[row][col] != 1:
                col -= 1
                row += 1

            if col >= 0 and row < self.number_of_queens and board[row][col] == 1:
                attacking += 1

            # Check right up Diagonal
            row = state[i] - 1
            col = i + 1
            while col < self.number_of_queens and row >= 0 and board[row][col] != 1:
                col += 1
                row -= 1

            if col < self.number_of_queens and row >= 0 and board[row][col] == 1:
                attacking += 1

        return int(attacking / 2)


    def generate_board(self,board, state):
        self.board_reset(board)
        for i in range(self.number_of_queens):
            board[state[i]][i] = 1


    def copy_state(self, state1, state2):
        state1[:] = state2[:]


    def get_neighbour(self,board, state):
        
        
        op_Board = [[0] * self.number_of_queens for _ in range(self.number_of_queens)]
        op_state = [0] * self.number_of_queens

        self.copy_state(op_state, state)
        self.generate_board(op_Board, op_state)

        opObjective = self.find_heuristic(op_Board, op_state)

        neighbour_board = [[0] * self.number_of_queens for _ in range(self.number_of_queens)]
        neighbour_state = [0] * self.number_of_queens

        self.copy_state(neighbour_state, state)
        self.generate_board(neighbour_board, neighbour_state)
        
        self.size += self.func_size(neighbour_board)

        for i in range(self.number_of_queens):
            for j in range(self.number_of_queens):
                if j != state[i]:
                    neighbour_state[i] = j
                    neighbour_board[neighbour_state[i]][i] = 1
                    neighbour_board[state[i]][i] = 0

                    temp = self.find_heuristic(neighbour_board, neighbour_state)

                    if temp <= opObjective:
                        opObjective = temp
                        self.copy_state(op_state, neighbour_state)
                        self.generate_board(op_Board, op_state)

                    neighbour_board[neighbour_state[i]][i] = 0
                    neighbour_state[i] = state[i]
                    neighbour_board[state[i]][i] = 1
                    
                    self.unique += 1
        print(opObjective)
        elapsed_time = self.timer() - self.start
        self.elapsed_times.append(elapsed_time)
        self.heuristic_values.append(opObjective)

        self.copy_state(state, op_state)
        self.board_reset(board)
        self.generate_board(board, state)
        
    def plot_hero(self):
        # Plotting
        plt.figure(figsize=(10, 5))
        plt.plot(self.elapsed_times,self. heuristic_values, marker='o', linestyle='-', color='b')
        plt.title('HillClimbing Heuristic Values over Time')
        plt.xlabel('Elapsed Time (seconds)')
        plt.ylabel('Heuristic Value')
        plt.grid(True)
        plt.show(block=False)


    def run(self):
        # self.pr.enable()
        self.start = self.timer()
        neighbour_board = [[0] * self.number_of_queens for _ in range(self.number_of_queens)]

        neighbour_state = [0] * self.number_of_queens
        


        self.copy_state(neighbour_state, self.state)
        self.generate_board(neighbour_board, neighbour_state)
        while True:
            self.copy_state(self.state, neighbour_state)
            self.generate_board(self.board, self.state)

            # Getting the optimal neighbour

            self.get_neighbour(neighbour_board, neighbour_state)

            if self.compare_states(self.state, neighbour_state):
                self.final_sol = self.board
                # self.print_board()
                break

            elif self.find_heuristic(self.board, self.state) == self.find_heuristic(
                neighbour_board, neighbour_state
            ):
                # Random neighbour
                index_1 = randint(0, self.number_of_queens - 1)
                index_2 = randint(0, self.number_of_queens - 1)

                neighbour_state[index_1], neighbour_state[index_2] = (
                    neighbour_state[index_2],
                    neighbour_state[index_1],
                )
                self.generate_board(neighbour_board, neighbour_state)
                self.number_of_tries += 1
        self.found_sol = True
        self.end = self.timer()
        
        # self.pr.disable()
        self.memory = (self.size + self.func_size(self.get_neighbour) / 1024)
        self.execution_time()
        # self.pr.print_stats()
        self.plot_hero()


# Driver code

# N = 4

# board = [[0] * N for _ in range(N)]
# state = [i for i in range(N)]

# hc = HellClimbing(N,board)
# hc.hillclimbing_solu()





