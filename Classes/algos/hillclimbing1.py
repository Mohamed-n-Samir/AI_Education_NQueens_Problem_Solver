# from __future__ import annotations
# from Classes.algos.performance import Performance
# import random

# def random_row(bound):
#     return random.choice(range(bound))

# class Queen():
#     def __init__(self,row,col) -> None:
#         self.__row = row
#         self.__col = col
    
#     def get_row(self) -> int:
#         return self.__row 
    
#     def get_col(self) -> int:
#         return self.__col
    
#     def move(self):
#         self.__row += 1
        
#     def is_conflict(self, queen: Queen):
        
#         # check rows and coloums
#         if self.__row == queen.get_row() or self.__col == queen.get_col():
#             return True
#         elif abs(self.__col-queen.get_col()) == abs(self.__row - queen.get_row()):
#             return True
#         return False
        
# class HellClimbing(Performance):
    
#     def __init__(self, size,board) -> None:
#         super().__init__()
#         self.n_queens = size
#         self.final_sol = board
#         self.heuristic = 0

#     def get_final_solution(self):  
#         return self.final_sol
    
#     # Method to Create a New Random Board
#     def generate_board(self): 
#         start_board = [0 for i in range(self.n_queens)]
#         for i in range(self.n_queens):
#             start_board[i] = Queen(random_row(self.n_queens),i)
#         return start_board
    
#     # Method to find Heuristics of a state
    
#     def find_heuristic(self,state: list):
#         heuristic = 0
#         for i in range(len(state)):
#             for j in range(i + 1,len(state)):
#                 if state[i].is_conflict(state[j]):
#                     heuristic += 1
#         return heuristic
    
#     # Method to get the next board with lower heuristic
    
#     def next_board(self,present_board: list):
#         next_board = [0 for i in range(self.n_queens)]
#         tmp_board = [0 for i in range(self.n_queens)]
#         present_heuristic = self.find_heuristic(present_board)
#         best_heuristic = present_heuristic
#         temp_h = 0
        
#         for i in range(self.n_queens):
            
#             # Copy present board as best board and temp board
#             next_board[i] = Queen(present_board[i].get_row(),present_board[i].get_col())
#             tmp_board[i] = next_board[i]
            
#         # Iterate each column
#         for i in range(self.n_queens):
#             if i > 0 :
#                 tmp_board[i-1] = Queen(present_board[i-1].get_row(),present_board[i-1].get_col())
#             tmp_board[i] = Queen(0,tmp_board[i].get_col())
            
#             # Iterate each row
#             for j in range(self.n_queens):
                
#                 # Get the heuristic Queen
#                 temp_h = self.find_heuristic(tmp_board)
                
#                 # Check if temp board better than best board
#                 if temp_h < best_heuristic:
#                     best_heuristic = temp_h
                    
#                     # Copy the temp board as best board
#                     for k in range(self.n_queens):
#                         next_board[k] = Queen(tmp_board[k].get_row(), tmp_board[k].get_col())
                
#                 # Move the queen 
#                 if not(tmp_board[i].get_row() == (self.n_queens - 1)):
#                     tmp_board[i].move()
        
#         # Check whether the present board adn teh best board found have same heuristic
#         # Then randomly generate new board and assign it to best board
#         if best_heuristic == present_heuristic:
#             next_board = self.generate_board()
#             self.heuristic = self.find_heuristic(next_board)
#         else :
#             self.heuristic = best_heuristic
#         return next_board
    
#     def run_search(self):
#         self.pr.enable()
#         self.start = self.timer()
#         present_board = self.generate_board()
#         present_heuristic = self.find_heuristic(present_board)
        
#         # test if the present board is the solution board
#         while not (present_heuristic == 0):
            
#             # Get the next board
#             present_board = self.next_board(present_board)
#             present_heuristic = self.heuristic
#             self.number_of_tries += 1
#         # self.final_sol = present_board 
#         # temp_board = [[0] * self.n_queens for _ in range(self.n_queens)]
#         for i in range(self.n_queens):
#             self.final_sol[present_board[i].get_row()][present_board[i].get_col()] = 1
#         self.found_sol = True
#         self.end = self.timer()
#         self.pr.disable()
#         self.execution_time()
#         self.pr.print_stats()


import random
import gc
import math
# from Classes.algos.performance import Performance

class Genetic():
    
    def __init__(self,number_of_queens,board) -> None:
        super().__init__()
        self.board_size = number_of_queens
        self.population_size = self.process_number(number_of_queens)
        self.generations = self.population_size * 10
        self.board = board
        
    
    def generate_individual(self,board_size):
        return random.sample(range(board_size), board_size)


    def fitness(self,individual):
        clashes = 0
        board_size = len(individual)

        for i in range(board_size):
            for j in range(i + 1, board_size):
                if individual[i] == individual[j] or abs(
                    individual[i] - individual[j]
                ) == abs(i - j):
                    clashes += 1

        return clashes


    def crossover(self,parent1, parent2):
        # point = random.randint(1, len(parent1) - 1)
        # child1 = parent1[:point] + [gene for gene in parent2 if gene not in parent1[:point]]
        # child2 = parent2[:point] + [gene for gene in parent1 if gene not in parent2[:point]]
        # return child1, child2
        n = len(parent1)
        c = random.randint(0, n - 1)
        return parent1[0:c] + parent2[c:n]

    # def crossover(parent1, parent2):
    #     # Uniform crossover
    #     child = [p1 if random.random() < 0.5 else p2 for p1, p2 in zip(parent1, parent2)]
    #     return child


    def mutate(self,individual):
        mutation_point = random.randint(0, len(individual) - 1)
        new_value = random.randint(0, len(individual) - 1)
        individual[mutation_point] = new_value
        return individual


    def genetic_algorithm(self):
        
        attempts = 0

        while True:
            population = [self.generate_individual(self.board_size) for _ in range(self.population_size)]
            best_fitness_stable_count = 0
            generation = 0

            while generation < self.generations:
                fitness_scores = [
                    (individual, self.fitness(individual)) for individual in population
                ]
                fitness_scores.sort(key=lambda x: x[1])

                best_solution, best_fitness = fitness_scores[0]
                print(f"Generation {generation + 1} - Best Fitness: {best_fitness}")

                if best_fitness == 0:
                    print("Solution Found:", best_solution)
                    return best_solution

                if generation == self.generations - 1:
                    if best_fitness < 3 and attempts < self.board_size // 3:
                        print(f"Best fitness less than 3. Increasing generations.")
                        self.generations += self.population_size  # Increase the number of generations
                        attempts += 1
                    else:
                        break
                
                if best_fitness > 3:

                    prev_best_fitness = fitness_scores[1][1]
                    if best_fitness == prev_best_fitness:
                        best_fitness_stable_count += 1
                    else:
                        best_fitness_stable_count = 0
                        attempts = 0

                    if best_fitness_stable_count > self.population_size:
                        print(
                            f"Restarting the algorithm as best fitness has been stable for {self.population_size} generations."
                        )
                        gc.collect()  # Manually trigger garbage collection
                        break

                parents = [
                    individual for individual, _ in fitness_scores[: self.population_size // 2]
                ]
                children = []
                while len(children) < self.population_size - len(parents):
                    parent1, parent2 = random.sample(parents, 2)
                    child1 = self.crossover(parent1, parent2)
                    child2 = self.crossover(parent1, parent2)
                    child1 = self.mutate(child1)
                    child2 = self.mutate(child2)
                    children.extend([child1, child2])
                        
                

                population = parents + children
                generation += 1

    def process_number(self,number):
        result = math.ceil(number * 1.6)
        result_rounded = math.ceil(result / 10) * 10
        return int(result_rounded)
    
    def assign_board(self,sol):
        for col in range(self.board_size):
            self.board[sol[col]][col] = 1
            
gen = Genetic(30,1)
gen.genetic_algorithm()





# Example Usage:
# board_size = 30
# population_size = process_number(board_size)
# generations = population_size * 10
# restart_threshold = int(board_size / 3)

# solution = genetic_algorithm(
#     board_size, population_size, generations, restart_threshold
# )

        
    
