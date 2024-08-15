# Initialize the first two terms of the Fibonacci sequence
n_1_term = 0  # First term (n=1)
n_2_term = 1  # Second term (n=2)

# Initialize the counter to keep track of which term we are currently on
count = 1  # Start with the first term

# Define a lambda function to sum two numbers, representing the addition step in Fibonacci
sum = lambda a, b: a + b

# Define a recursive function to calculate and print the Fibonacci sequence up to the nth term
def fib(nth_term, count, n_1_term, n_2_term):
    # Base cases to return the first or second term
    if (count == 1):
        num = n_1_term  # Return the first term if count is 1
    elif (count == 2):
        num = n_2_term  # Return the second term if count is 2
    else:
        # Calculate the next term in the sequence
        num = sum(n_1_term, n_2_term)  # Sum the two previous terms
        n_1_term = n_2_term  # Update the first previous term
        n_2_term = num  # Update the second previous term

    # If we haven't reached the nth term, continue recursion
    if (count != nth_term):
        count += 1  # Move to the next term
        print(num, end=" ")  # Print the current term on the same line
        return fib(nth_term, count, n_1_term, n_2_term)  # Recursive call with updated values
    else:
        return num  # Return the nth term

# Display a message to the user explaining what the program does
print("\nDisplaying Fibonacci numbers from the 1st term to the nth term. Taking the 1st term as 0.")

try:
    # Prompt the user to input the nth term they want to calculate
    nth_term = int(input("Enter nth term: "))

    # Check if the input is a positive integer
    if (nth_term > 0):
        # Call the fib function and print the result (the nth Fibonacci number)
        print(f"{fib(nth_term, count, n_1_term, n_2_term)} \n")
    else:
        # If the user enters a non-positive number, display an error message
        print("Enter nth term greater than 0") 
except ValueError as e:
    # If the user input is not an integer, catch the ValueError and display a custom error message
    print(f'Invalid Value: {e}')
