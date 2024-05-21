def CanPlace(X, j):
    for i in range(1, j):
        if X[i] == X[j] or abs(X[i] - X[j]) == abs(i - j):
            return False
    return True

def n_Queen1(X, i, n, solutions):
    if CanPlace(X, i):
        if i == n:
            solutions.append(X[1:n+1].copy())
        else:
            for k in range(1, n + 1):
                X[i + 1] = k
                n_Queen1(X, i + 1, n, solutions)

def solve_n_queens(n):
    X = [0] * (n + 1)  # We use 1-based indexing
    solutions = []
    n_Queen1(X, 0, n, solutions)
    return solutions

# Example usage:
n = 4
solutions = solve_n_queens(n)
for solution in solutions:
    print(solution)
