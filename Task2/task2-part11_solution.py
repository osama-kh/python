#auther: osama khwaled


# 2.a
def my_filter(f):
    """
    this function is filter for a given list that
    return a new list with a values that true

    """
    def list_i(list1):
         lists = []
         for i in range(len(list1)):
              if f(list1[i]):
                  lists.append(list1[i])
         return lists
    return list_i

'''
list =[1 ,2 ,3 ,4 ,5]
print(my_filter.__doc__, my_filter(lambda x : x %2==0)(list))
'''


# 2.b
def filtered_words(words, n):
    """
    :param words: list of words
    :param n: the restrict of the length
    :return: list with more length than n

    """
    for i in range(len(words)):
        x = words[i]
        return my_filter(lambda x: len(x) > n)(words)


#list = ['Hello', 'Hi', 'python', 'a', 'ABCDE']
#print(filtered_words.__doc__, filtered_words(list, 1))


# 2.c

def my_map(f):
    """

    :param lst: list of values
    :param f: function
    :return: list of the values of the old list that get into the f function

    """
    def mapx(lst):
        temp=[]
        for i in range(len(lst)):
             temp.append(f(lst[i]))
        return temp
    return mapx

#list=[1,2,3,4,5,6]
#print(my_map.__doc__,my_map(lambda x:x*3)(list))

#2.d



def my_filter_and_map(lst,f1,f2):
    """

    :param lst: list of values
    :param f1: boolean function
    :param f2: function
    :return: return a list with values that do the terms of the both functions

    """
    lists= my_filter(f1)(lst)
    listf= my_map(f2)(lists)
    return listf

#list =[1 ,2 ,3 ,4 ,5]
#print(my_filter_and_map.__doc__,my_filter_and_map(list,lambda x : x %2==0,lambda x:x**2))


# 3
def polynomial(factors):
    """
    :param factors: list of values
    :return: the result op polynomial operation

    """

    def insert(x):
        sum = 0
        for i in range(len(factors)):
            sum += int(factors[len(factors) - i - 1] * (x ** i))
        return sum

    return insert


#list = [1, 2, 1, 0]
#polynom = polynomial(list)
#value = polynom(4)
#print(polynomial.__doc__,value)

#############################################################
#Game


import random


def f1(x):
    '''

    :param x:
    :return: if x bigger than the random number return true
    '''
    def score(gnum):
        return int(x) >= int(gnum)

    return score


def f2(x):
    '''

    :param x:
    :return: if x smaller than the random number return true
    '''
    def score(gnum):
        return int(x) <= int(gnum)

    return score
'''
f3:return sum of th random number digits
f3:return minus of th random number digits
'''

f3 = (lambda gnum: int(gnum // 10000 + (gnum // 1000) % 10 + (gnum // 100) % 10 + (gnum // 10) % 10 + gnum % 10))
f4 = (lambda gnum: int(gnum // 10000 - (gnum // 1000) % 10 - (gnum // 100) % 10 - (gnum // 10) % 10 - gnum % 10))


def f5(num):  # with no print odd even
    '''

    :param num:
    :return: print the even digits as"x" and the odd "-"
    '''
    for i in range(5):
        if num % 2 == 0:
            print("x", end="")
        else:
            print("-", end="")
        num = num // 10


def f6(num):  # with no print %3
    '''

    :param num:
    :return: print the  digits%3==0 as"x" else "-"
    '''
    if (num // 10000) % 3 == 0:
        print("x", end="")
    else:
        print("-", end="")

    if (num // 1000) % 10 == 0:
        print("x", end="")
    else:
        print("-", end="")

    if (num // 100) % 10 % 3 == 0:
        print("x", end="")
    else:
        print("-", end="")

    if (num // 10) % 10 % 3 == 0:
        print("x", end="")
    else:
        print("-", end="")

    if (num % 10) % 3 == 0:
        print("x", end="")
    else:
        print("-", end="")


def yes_or_no(f, n):
    '''

    :param f: for f1 f2
    :param n:
    :return: yes/no
    '''
    def x(gnum):
        yes = "Yes"
        no = "No"
        if f(n)(gnum) == True:
            return yes
        else:
            return no

    return x


def print_msg_to_func(msg, f):
    '''
    :param msg: print massage
    :param f: for f3/f4
    :return: print msg
    '''
    if f:
        print(msg)


def show_string_by_func(msg, f):
    '''

    :param msg: print massage
    :param f:for f5/f6
    :return: the functions value
    '''
    def rf(gnum):
        if f:
            print(msg, end="")
        return f(gnum)

    return rf




def code_cracker():
    '''
    the main function to play the game
    '''
    print("Welcome to the pin cracker game!")
    gnum = random.randrange(10000, 99999, 1)
    score = 100

    for i in range(10):
        # while(score!=0 or input()):
        print("clue#", i + 1)
        choice = int( random.randrange(1, 6, 1))

        if choice == 1:
            print("Enter a Number to check if the code is")
            print("smaller: ")
            value = int(input())
            print(yes_or_no(f1, value)(gnum))
            if yes_or_no(f1, value)(gnum) == "No":
                score -= 10
            print("points left: ", score)
            if value == gnum:
                print("\nyes, correct!")
                print("points left: ", score)
                exit(1)
            value = input("\nguess or press ENTER for exit:\n")
            if not value:
                print("\nwrong,bye bye!")
                print("points left: ", score)
                break
                exit(1)

        if choice == 2:
            print("Enter a Number to check if the code is")
            print("bigger: ")
            value = int(input())
            print(yes_or_no(f2, value)(gnum))
            if yes_or_no(f2, value)(gnum) == "No":
                score -= 10
            print("points left: ", score)
            if value == gnum:
                print("\nyes, correct!")
                print("points left: ", score)
                exit(1)
            value = input("\nguess or press ENTER for exit:\n")
            if not value:
                print("\nwrong,bye bye!")
                print("points left: ", score)
                break
                exit(1)

        if choice == 3:
            print_msg_to_func("sum: ", f3)
            value = int(input())
            if f3(gnum) != value:
                score -= 10
            print("points left: ", score)
            if value == gnum:
                print("\nyes, correct!")
                print("points left: ", score)
                exit(1)
            value = input("\nguess or press ENTER for exit:\n")
            if not value:
                print("\nwrong,bye bye!")
                print("points left: ", score)
                break
                exit(1)

        if choice == 4:
            print_msg_to_func("sub: ", f4)
            value = int(input())
            if f4(gnum) != value:
                score -= 10
            print("points left: ", score)
            if value == gnum:
                print("\nyes, correct!")
                print("points left: ", score)
                exit(1)
            value = input("\nguess or press ENTER for exit:\n")
            if not value:
                print("\nwrong,bye bye!")
                print("points left: ", score)
                break
                exit(1)

        if choice == 5:
            show_string_by_func("odd digits: ", f5)(gnum)
            value = input("\nguess or press ENTER for exit:\n")
            print("points left: ", score)
            if value == gnum:
                print("\nyes, correct!")
                print("points left: ", score)
                exit(1)
            if not value:
                print("\nwrong,bye bye!")
                print("points left: ", score)
                break
                exit(1)
            if gnum != value:
                score -= 10

        if choice == 6:
            show_string_by_func("digits divided by 3: ", f6)(gnum)
            value = input("\nguess or press ENTER for exit:\n")
            print("points left: ", score)
            if value == gnum:
                print("\nyes, correct!")
                print("points left: ", score)
                exit(1)
            if not value:
                print("\nwrong,bye bye!")
                print("points left: ", score)
                break
                exit(1)
            if gnum != value:
                score -= 10

        if score==0:
            print("\nwrong,bye bye!")





