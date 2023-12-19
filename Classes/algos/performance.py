import cProfile
# import numpy as np
# import matplotlib as plt
from timeit import default_timer as timer

# import psutil
import time,sys
# import resource


class Performance :
    def __init__(self) -> None:
        self.pr = cProfile.Profile()
        self.timer = timer
        self.time_in_sec = 0
        self.start = 0
        self.end = 0
        self.number_of_tries = 1
        self.found_sol = False
        self.memory = 0
        self.unique = 0
        self.algorithm = ''
        

        
    def execution_time(self):
        print("Execution time:", self.end - self.start, "seconds")
        print("Number of Tries: ", self.number_of_tries)
        print("Found Solution??: ", self.found_sol)
        self.time_in_sec = self.end - self.start
        
    def func_size(self,func):
        return sys.getsizeof(func)
        
        
    # def get_memory_usage(self):
    #     # Get memory usage in kilobytes
    #     return psutil.Process().memory_info().rss
    
    # def sleep(self,seconds):
    #     time.sleep(seconds)
        
    # def measure_memory(self,func,*args, **kwargs):
    #     start_rusage = resource.getrusage(resource.RUSAGE_SELF)
    #     result = func(*args, **kwargs)
    #     time.sleep(0.1)
    #     end_rusage = resource.getrusage(resource.RUSAGE_SELF)
    #     self.memory += (end_rusage.ru_maxrss - start_rusage.ru_maxrss)
    #     if end_rusage.ru_maxrss == start_rusage.ru_maxrss :
    #         self.memory += start_rusage.ru_maxrss
    #     print(f"Memory used: {self.memory } KB")
    #     return result
        
        
        