#   Program to print fibonacci numbers from n = 1 to the given nth term
n_1_term = 0
n_2_term = 1
count = 1
sum = lambda a, b: a + b

def fib(nth_term, count, n_1_term, n_2_term):
    if (count == 1):
        num = n_1_term
    elif (count == 2):
        num = n_2_term
    else:
        num = sum(n_1_term, n_2_term)
        n_1_term = n_2_term
        n_2_term = num
    if (count != nth_term):
        count+=1
        print(num, end=" ")
        return fib(nth_term, count, n_1_term, n_2_term)
    else:
        return num


print("Displaying fibonacci numbers from the 1st term to the nth term\n\
    Taking the 1st term as 0.")

try:
    nth_term = int(input("Enter nth term: "))
    if (nth_term > 0):
        print(fib(nth_term, count, n_1_term, n_2_term))
    else:
        print("Enter nth term greater than 0") 
except ValueError as e:
    print(f'Invalid Value {e}')







