#auther: osama khwaled



def Xnor(v1, v2):
    """
       Question number 1.
       xnor function.
       Parameters list: v1,v2.
       Return value : True/False.
       """
    if bool(v1) == bool(v2):
        return True
    else:
        return False


print(Xnor.__doc__)
print(Xnor(True, False))
print(Xnor(9 > 5, 3 < 4))
print(Xnor(9 < 5, 3 == 4))
print(Xnor(9 < 5, 3 < 4))
x = input()
y = input()
print(Xnor(x, y))


#############################################################################################

def counter(var):
    count = 0
    Test = var

    for i in range(5):
        Test = int(Test / 10)
        count = count + 1
        if Test == 0:
            return count
            break


def Digits(var):
    """
       Question number 2.
       Digits function.
       Parameters list: var.
       Return value : size of number and if odd or even.
       """
    if counter(var) > 5 or var < 0:
        print("Error!")
    else:
        if counter(var) == 1:
            if var % 2 == 0:
                print("one digit  -even")
            else:
                print("one digit  -odd")

        if counter(var) == 2:
            x = int(var / 10) + int(var % 10)
            if x % 2 == 0:
                print("two digit  -even")
            else:
                print("two digit  -odd")

        if counter(var) == 3:
            x = int(var / 100) + int(var % 10)
            if x % 2 == 0:
                print("three digit  -even")
            else:
                print("three digit  -odd")

        if counter(var) == 4:
            print(int((var / 100) % 10), int((var % 100) / 10))

            x = int((var / 100) % 10) + int((var % 100) / 10)
            if x % 2 == 0:
                print("four digit  -even")
            else:
                print("four digit  -odd")

        if counter(var) == 5:
            if int((var % 1000) / 100) % 2 == 0:
                print("five digit  -even")
            else:
                print("five digit  -odd")


print(Digits.__doc__)
var = int(input("enter a number with digits between 1-5:  "))
print(Digits(var))


#############################################################################################

def counter(var):
    count = 0
    Test = var

    for i in range(var):
        Test = int(Test / 10)
        count = count + 1
        if Test == 0:
            return count
            break


def Good_order(num):
    """
       Question number 3.
       Good order function.
       Parameters list: num.
       Return value : true if all the digits even or odd else false.
       """
    count_even: int = 0
    count_odd: int = 0
    test = num
    for i in range(int(counter(num))):
        if test % 2 == 0:
            count_even = count_even + 1

        if test % 2 != 0:
            count_odd = count_odd + 1

        test = int(test / 10)

    if count_even == counter(num) or count_odd == counter(num):
        return True
    else:
        return False


print(Good_order.__doc__)
num = int(input("enter a number :"))
print(Good_order(num))


#############################################################################################


def Figure(size):
    """
       Question number 4.
       FigUre function.
       Parameters list: num.
       Return value : print the triangle.
       """
    if 0 < size < 10:

        for row in range(1, size + 1):
            for col in range(1, size * 2):
                x = int(size - col)
                if x < 0:
                    x = x * -1
                if (size + 1 == col + row or col - row == size - 1) and row != size:
                    print(row, end="")

                elif row == size:
                    print(x + 1, end="")
                else:
                    print(" ", end="")

            print("")


print(Figure.__doc__)
num = int(input("enter a number to build a hologram triangle :"))
print(Figure(num))


#############################################################################################

def num_of_digits(var):
    if var < 10:
        return 1
    else:
        return 1 + num_of_digits(var / 10)


def biggest_digit(var):
    if var / 10 == 0:
        return var % 10
    else:
        return max(var % 10, biggest_digit(int(var / 10)))


def weight(num):
    """
         Question number 5.
         weight function.
         Parameters list: num.
         Return value : the numbers weight=number of digits+largest digit.
         """
    return biggest_digit(num) + num_of_digits(num)


print(weight.__doc__)
number = int(input("enter a value to know it's weight:"))
print(weight(number))


#############################################################################################


def IsPrimary(num, indx=2):
    """
       Question number 6.
       IsPrimary function.
       Parameters list: num.
       Return value : true if the number is prime else false  .
       """
    if indx > num / 2:
        return True

    elif num % indx == 0:
        return False

    else:
        return IsPrimary(num, indx + 1)


print(IsPrimary.__doc__)
x = int(input("Enter a value:"))
print(IsPrimary(x))


#############################################################################################



def Reduce(num):
    """
       Question number 7.
       Reduce function.
       Parameters list: num.
       Return value : number without zero's .
       """
    if num == 0:
        return 0
    test=num
    if num<0:
        num*=-1
    sto= Reduce(int(num/10))
    if num%10!=0:
        sto*=10
        sto+=num%10
    num = sto
    if test < 0:
        num *= -1
    return num


print(Reduce.__doc__)
var = int(input("enter a number :  "))
print(Reduce(var))

#############################################################################################

def Factorial(num):
    if num == 0:
        return 1
    total = num * Factorial(num - 1)
    return total


def Pascal(m, n):
    """
       Question number 8.
       Pascal and Factorial function.
       Parameters list: num ,n ,m.
       Return value : the value that exist in the input coordination in pascal triangle  .
       """
    if n > m:
        return -1
    else:
        return int(Factorial(m) / (Factorial(m - n) * Factorial(n)))


print(Pascal.__doc__)
n = int(input("enter the raw coordination:  "))
m = int(input("enter the column coordination:  "))
print(Pascal(m, n))
