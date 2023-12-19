import random
import gc
import math
from Classes.algos.performance import Performance
from matplotlib import pyplot as plt 

class Genetic(Performance):
    
    def __init__(self,number_of_queens,board) -> None:
        super().__init__()
        self.board_size = number_of_queens
        self.population_size = self.process_number(number_of_queens)
        self.generations = self.population_size * 10
        self.board = board
        self.algorithm = "Genetic"
        self.size = 0
        self.heuristic_values = []
        self.elapsed_times = []

        
    
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
        n = len(parent1)
        c = random.randint(0, n - 1)
        return parent1[0:c] + parent2[c:n]
    

    def mutate(self,individual):
        mutation_point = random.randint(0, len(individual) - 1)
        new_value = random.randint(0, len(individual) - 1)
        individual[mutation_point] = new_value
        return individual


    def gen_algo(self):
        
        attempts = 0

        while True:
            population = [self.generate_individual(self.board_size) for _ in range(self.population_size)]
            self.size += self.func_size(population)
            best_fitness_stable_count = 0
            generation = 0
            

            while generation < self.generations:
                fitness_scores = [
                    (individual, self.fitness(individual)) for individual in population
                ]
                fitness_scores.sort(key=lambda x: x[1])

                best_solution, best_fitness = fitness_scores[0]
                print(f"Generation {generation + 1} - Best Fitness: {best_fitness}")
                self.unique += 1
                
                self.heuristic_values.append(best_fitness)
                elapsed_time = self.timer() - self.start
                self.elapsed_times.append(elapsed_time)
                

                if best_fitness == 0:
                    print("Solution Found:", best_solution)
                    self.assign_board(best_solution)
                    return best_solution

                if generation == self.generations - 1:
                    if best_fitness < 3 and attempts < 10:
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
                        self.number_of_tries += 1
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
            self.number_of_tries += 1
                

        
    def run(self):
        self.start = self.timer()
        ans = self.gen_algo()
        self.end = self.timer()
        self.execution_time()
        self.memory = self.size + self.func_size(self.run)
        self.plot_hero()
        return ans

    def process_number(self,number):
        result = math.ceil(number * 1.6)
        result_rounded = math.ceil(result / 10) * 10
        return int(result_rounded)
    
    def assign_board(self,sol):
        for col in range(self.board_size):
            self.board[sol[col]][col] = 1
            
    def plot_hero(self):
        # Plotting
        plt.figure(figsize=(10, 5))
        plt.plot(self.elapsed_times,self.heuristic_values, marker='o', linestyle='-', color='b')
        plt.title('Genetic Heuristic Values over Time')
        plt.xlabel('Elapsed Time (seconds)')
        plt.ylabel('Heuristic Value')
        plt.grid(True)
        plt.show(block=False)

