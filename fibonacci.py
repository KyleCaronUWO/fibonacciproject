# Fibonacci Sequence Script
#Created by Kyle Caron

# Take amount of numbers and place in int

amount = int(input("Please enter how many numbers you want:"))

# Declared variables
# Fib = starting number
# Fib2 = next number in sequence
# Loop = amount of loops that user has put in

fib = 0
fib2 = 1
loop = amount

# For statement dictating for each loop in the amount print the first number, then move to next number in sequence while adding previous number and continues loop until end

for loop in range(amount):
    print(fib)
    fibnext = fib + fib2
    fib = fib2
    fib2 = fibnext
    
    

