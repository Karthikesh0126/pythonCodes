def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Example usage:
terms = 10
fib_sequence = fibonacci(terms)
print(f"Fibonacci Sequence of {terms} terms: {fib_sequence}")