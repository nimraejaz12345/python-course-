# Program to print Fibonacci series up to n terms

# Taking input from the user
n = int(input("Enter the number of terms: "))

# First two Fibonacci numbers
first = 0
second = 1

print("Fibonacci Series:")

# Loop to print Fibonacci series
for i in range(n):
    print(first, end=" ")

    # Finding the next term
    next_term = first + second

    # Updating values
    first = second
    second = next_term