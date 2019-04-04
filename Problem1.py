__author__ = 'arinmukherjee'

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.



def check3mult(x):
        if x%3 == 0:
                return(True)

def check5mult(x):
        if x%5 == 0:
                return(True)


sum = 0
x = 1

while x < 1000:
        if check3mult(x) == True or check5mult(x) == True:
                sum += x
        x += 1

print(sum)
