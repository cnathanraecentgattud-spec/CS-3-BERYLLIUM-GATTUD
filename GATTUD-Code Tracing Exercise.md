
# CODE 1
def greet_students(name,nChar):
    for i in range(nChar):
        print(name[i])

name = input("Enter a Name: ")
nChar = input("Enter any numeric number: ")
nChar = int(nChar)
greet_students(name, nChar)

# a. If name is “Joseph The Dreamer” and nChar is 5, what will be the output of the code above and why?
# The output of the code would be the first five characters of "Joesph" stacked vertically on separate lines, as the name would be looped and displayed per character depending on what value is placed for nChar.

# b. Using the same name and nChar is 20, what now is the output and why?
# A string index out of range error would occur, since putting 20 as nChar would cause the system to reach of letters beyond what it was provided, resulting in an IndexError.

# c. If there is an error message encountered in letter b, how will you be able to modify the code so that the error message will not appear.
# Configure the name to reach 20 or more characters, or lessen the value of nChar to be within the length of the fed name. 

# CODE 2
def greet_students(name, nChar):
    for i in range(nChar):
        print(name[i : nChar])  # Adjusted to print the substring from index i to nChar

name = input("Enter a Name: ")
greet_students(name, len(name))

# Adjustments
# added "":"" to line 2 range function
# swapped the [0 : nChar] to [i : nChar] to print the name from index i to nChar, allowing for counted characters to be removed per iteration cycle instead of printing the whole name nChar times.

# CODE 3

def squaring_list(n):
    squares = []
    for i in range(1, n + 1):
        squares.append(i ** 2)
    return squares

def sum_list(squares):
    total = 0
    for square in squares:
        total += square
    return total

n = 0
while n < 1 or n > 100:
    n = input("Enter a Number from 1 to 100: ")
    n = int(n)

print(f"Sum of all squared numbers is {sum_list(squaring_list(n))}.")


