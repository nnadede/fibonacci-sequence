#   Program to print fibonacci numbers from n = 1 to the given nth term
n_1_term = 0
n_2_term = 1
count = 0
sum = lambda a, b: a + b

def fib(nth_term):
    if (count == 0):
        num = n_1_term
    elif (count == 1):
        num = n_2_term
    else:
        num = sum(n_1_term, n_2_term)
        n_1_term = n_2_term
        n_2_term = num
    if (count != nth_term):
        return fib(nth_term)
    else:
        return num


print("Displaying fibonacci numbers from the 1st term to the nth term\n\
    Taking the 1st term as 0.")

nth_term = int(input("Enter nth term: "))

try:
    if (nth_term > 0):
        print(fib(nth_term))
    else:
        raise ValueError("Enter nth term greater than 0") 
except:
    print("Invalid Value")







