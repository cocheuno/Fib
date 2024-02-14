# Define a function to calculate Fibonacci numbers
def fibonacci(n):
    # Initialize variables for the first two Fibonacci numbers
    fib = [0, 1]

    # Loop from the 3rd Fibonacci number up to the nth Fibonacci number
    for i in range(2, n):
        # Calculate the next Fibonacci number by adding the previous two numbers
        fib.append(fib[-1] + fib[-2])

    # Return the list of Fibonacci numbers
    return fib

# Call the fibonacci function with argument 5 to get the first 5 Fibonacci numbers
fibonacci_numbers = fibonacci(9)

# Print the first 5 Fibonacci numbers
print("Thee first 5 Fibonacci numbers are:", fibonacci_numbers)
