def getFactors(num):
    """Returns a list of factors of the given number x.
    Basically, finds the numbers between 1 and the given integer that divide the number evenly.

    For example:
    - If we call getFactors(2), we'll get [1, 2] in return
    - If we call getFactors(12), we'll get [1, 2, 3, 4, 6, 12] in return
    """

    # your code here
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


num = int(input("Calculate the factors of: "))
print(getFactors(num))


def isPrime(x):
    """Returns whether or not the given number x is prime.

    A prime number is a natural number greater than 1 that cannot be formed
    by multiplying two smaller natural numbers.

    For example:
    - Calling isPrime(11) will return True
    - Calling isPrime(71) will return True
    - Calling isPrime(12) will return False
    - Calling isPrime(76) will return False
    """

    # your code here
    if x == 0 or x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, x):
        if (x % i == 0):
            return False
    else:
        return True


# Reading number
number = int(input('Enter number: '))
# Making decision
if isPrime(number):
    print('%d is Prime.' % (number))
else:
    print('%d is NOT Prime.' % (number))


def isComposite(x):
    """Returns whether or not the given number x is composite.

    A composite number has more than 2 factors.
    A natural number greater than 1 that is not prime is called a composite number.
    Note, the number 1 is neither prime nor composite.

    For example:
    - Calling isComposite(9) will return True
    - Calling isComposite(22) will return True
    - Calling isComposite(3) will return False
    - Calling isComposite(41) will return False
    """

    # your code here
    if x == 2:
        return False
    if x == 0 or x == 1:
        return False
    for i in range(2, x):
        if (x % i == 0):
            return True
    else:
        return False


# Reading number
number = int(input('Enter number: '))
# Making decision
if isComposite(number):
    print('%d is Composite.' % (number))
else:
    print('%d is NOT Composite.' % (number))


def isPerfect(x):
    """Returns whether or not the given number x is perfect.

    A number is said to be perfect if it is equal to the sum of all its
    factors (for obvious reasons the list of factors being considered does
    not include the number itself).

    Example: 6 = 3 + 2 + 1, hence 6 is perfect.
    Example: 28 is another example since 1 + 2 + 4 + 7 + 14 is 28.
    Note, the number 1 is not a perfect number.
    """

    # your code here
    factor = 0
    if x == 2:
        return False

    for i in range(1, x):
        if (x % i == 0):
            factor += i
    if factor == x:
        return True
    else:
        return False


# Reading number
number = int(input('Enter number: '))
# Making decision
if isPerfect(number):
    print('%d is Perfect.' % (number))
else:
    print('%d is NOT Perfect.' % (number))


def isTriangular(x):
    """Returns whether or not a given number x is triangular.

    The triangular number Tn is a number that can be represented in the form of a triangular
    grid of points where the first row contains a single element and each subsequent row contains
    one more element than the previous one.

    We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

    Example: 3 is triangular since 3 = 2(3) / 2
    3 --> 2nd position: (2 * 3 / 2)

    Example: 15 is triangular since 15 = 5(6) / 2
    15 --> 5th position: (5 * 6 / 2)
    """

    # your code here
    if x == 0 or x == 1:
        return True

    triangular_sum = 0
    for i in range(x):
        triangular_sum += i
        if triangular_sum == x:
            return True
        if i == x:
            return False


# Reading number
number = int(input('Enter number: '))
# Making decision
if isTriangular(number):
    print('%d is TRIANGULAR.' % (number))
else:
    print('%d is NOT TRIANGULAR.' % (number))


def isNarcissistic(x):
    """Returns whether or not a given number is Narcissistic.

    A positive integer is called a narcissistic number if it
    is equal to the sum of its own digits each raised to the
    power of the number of digits.

    Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
    Note that by this definition all single digit numbers are narcissistic.
    """

    # your code here

    pw = len(str(x))
    s = x
    su = 0
    while (x != 0):
        p = x % 10
        su += p ** (pw)
        x = x // 10
    if su == s:
        return True
    else:
        return False


number = int(input('Enter number: '))
# Making decision
if isNarcissistic(number):
    print('%d is Narcissistic.' % (number))
else:
    print('%d is NOT Narcissistic.' % (number))







