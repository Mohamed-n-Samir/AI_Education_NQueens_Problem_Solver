from memory_profiler import profile, memory_usage

@profile
def recursive_function(n):
    if n == 0:
        return 0
    return n + recursive_function(n - 1)

if __name__ == "__main__":
    mem_usage = memory_usage(lambda: recursive_function(5), interval=0.1)

    print("Memory Usage:", mem_usage)