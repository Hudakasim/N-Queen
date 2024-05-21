import time
import platform

# Function to check if a queen can be placed in the given column
def can_place(X, j):
    for i in range(1, j):
        if X[i] == X[j] or abs(X[i] - X[j]) == abs(i - j):
            return False
    return True

# Recursive function to solve the N-Queen problem using backtracking
def n_queen(X, i, n, solution_found):
    if solution_found[0]:  # If a solution is already found, terminate further processing
        return True
    if i == n:  # All queens are placed successfully
        solution_found[0] = True
        return True
    else:
        for k in range(1, n + 1):
            X[i + 1] = k
            if can_place(X, i + 1):
                if n_queen(X, i + 1, n, solution_found):
                    return True
    return False

# Function to initiate solving the N-Queen problem
def solve_n_queen(n):
    X = [0] * (n + 1)  # Initialize the board with zeroes
    solution_found = [False]  # Flag to indicate if a solution has been found
    n_queen(X, 0, n, solution_found)

# Function to measure the time taken to solve the N-Queen problem for a given size n
def solve_and_time_n_queen(n):
    start_time = time.time()
    solve_n_queen(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

# Function to find the maximum value of n before encountering a memory error
def find_memory_limit():
    n = 1
    while True:
        try:
            elapsed_time = solve_and_time_n_queen(n)
            print(f"Time taken to solve n= {n}: {elapsed_time:.10f} seconds")
            n += 1
        except MemoryError:
            print(f"MemoryError at n={n}")
            break

print("Python version used: ", platform.python_version())
print("****************************************")
find_memory_limit()
