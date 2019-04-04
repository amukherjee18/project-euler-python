__author__ = 'arinmukherjee'


# Just parsing through all numbers, checking to see if there prime takes too long
# Even checking if there prime by comparing to a list of previous primes takes too long

# Instead, I tried to maximize (kinda) the number of primes I could find in a reasonable amount of time
# (all primes less that 1 million)
# I then initialized a boolean array to all Trues, each index corresponding to a number between 1 (2) and
# (1,999,999) 2 million
# For every multiple of each of the primes I found, I set all the corresponding indexes in the array to false.
# At this point, if an element of the boolean array is false, it is not prime.
# If it is true, it is either prime or it is greater than 1 million and may or may not be prime
# Then I check these numbers, while appending every prime found to a list of known primes.
# Process finishes quickly


def divisible(num, by):
    if num%by == 0:
        return True
    return False


# doesn't work for 1 but isn't in scope of problem anyways
def check_prime(num):
    # check if 2
    if num == 2:
        return True

    # check if even or if it is 1 (this will never be the case
    if divisible(num,2): # or num == 1:
        return False

    # check odd numbers in range 3 to sqrt(num)
    for i in range(3,int(num**(0.5)) + 1, 2):
        if divisible(num, i):
            return False
    return True


sum = 2
known_primes = []


# doesn't count 2
def all_primes_under(num):
    # sum already has 2

    for i in range(3, num):
        if check_prime(i):
            global sum
            sum += i
            global known_primes
            known_primes.append(i)
    return known_primes



possibly_prime = []
#prime_index is number - 2
# number is prime_index + 2

def initialize_possibly_prime_list():
    global possibly_prime
    for i in range(2, 2000000):
        possibly_prime.append(True)


def set_all_multiples_of_two_to_false():
    global possibly_prime
    for i in range(2, len(possibly_prime), 2):
        possibly_prime[i] = False


def set_all_multiples_of_primes_under_to_false(num):
    all_primes_under(num)
    global known_primes

    set_all_multiples_of_two_to_false()

    # This increment ensures that even numbers are not looked at. (they have already been marked as false)
    for i in range(0, len(known_primes)):
        index_of_first = known_primes[i] - 2
        increment = 2 * known_primes[i]
        starting_index = index_of_first + 2 * increment

        global possibly_prime
        for j in range(starting_index, len(possibly_prime), increment):
            possibly_prime[j] = False

def index(num):
    return num - 2

def num(index):
    return index + 2

def check_prime_after(num):
    global known_primes

    # This means num > last element of known_prime
    start = known_primes[len(known_primes) - 1]
    # Don't check num
    for divisor in range(start, num, 2):
        if num % divisor == 0:
            return False

    known_primes.append(num)
    return True


first_threshold = 1000000
final_threshold = 2000000

initialize_possibly_prime_list()
set_all_multiples_of_primes_under_to_false(1000000)
print sum


# parse_through_rest
start = index(first_threshold) - 1 # this is 999,999, which is not prime so not overcounting
# Want to start with odd number, so can increment by 2
end = index(final_threshold)

for i in range(start, end + 1, 2):
    print 1.0*num(i)/final_threshold
    if possibly_prime[i] == True and check_prime_after(i):
        sum += num(i)

print sum
