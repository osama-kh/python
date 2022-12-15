import math
import functools


# q1
def make_rectangle(x, y, legnth, width):
    """
    make a new rectangle and add its coordination and its width and length
    """

    def dispatch(i):
        if i == 0:
            return x
        elif i == 1:
            return y
        elif i == 2:
            return legnth
        elif i == 3:
            return width

    return dispatch


r1 = make_rectangle(3, 4, 10, 26)


# print(r1)


def x(r):
    """
    return coordination x of the rectangle
    """
    return r(0)


def y(r):
    """
    return coordination x of the rectangle
    """
    return r(1)


def legnth(r):
    """
    return  legnth of the rectangle
    """
    return r(2)


def width(r):
    """
    return  width of the rectangle
    """
    return r(3)


def diagonal(r):
    """
    return the diagonal of the rectangle
    """
    return (legnth(r) ** 2 + width(r) ** 2) ** 0.5


def print_rectangle(r):
    """
    print the details of the rectangle
    """
    print("Rectangle: point = (", x(r), ",", y(r), "); size = ", legnth(r), "x", width(r))


def center(r):
    """
    return coordination  of the rectangle center
    """
    cx = (legnth(r) / 2) + x(r)
    cy = (width(r) / 2) + y(r)
    c = (cx, cy)
    return c


def distance(r1, r2):
    """
    return the distance between two rectangles
    """
    cr1 = center(r1)
    cr2 = center(r2)
    dis = ((cr1[0] - cr2[0]) ** 2 + (cr1[1] - cr2[1]) ** 2) ** 0.5
    return dis


def move(r1, deltaX, deltaY):
    """
    change the coordination of rectangle
    """
    return make_rectangle(x(r1) + deltaX, y(r1) + deltaY, legnth(r1), width(r1))


def resize(r1, factor):
    """
    change the size of the rectangle
    """
    return make_rectangle(x(r1), y(r1), legnth(r1) * factor, width(r1) * factor)


r2 = make_rectangle(6, 9, 5, 8)


def average_rectangle(r1, r2):
    """
    get the average of two rectangles
    """
    return make_rectangle((x(r1) + x(r2)) / 2, (y(r1) + y(r2)) / 2, (legnth(r1) + legnth(r2)) / 2,
                          (width(r1) + width(r2)) / 2)


###################################################################################################

# q2

def make_vector(size, list):
    """
    build a new vector
    """

    def dispatch(i):
        if i == 0:
            return size
        elif i == 1:
            return list

    return dispatch


v1 = make_vector(5, (1, 2, 3, 4, 5))
v2 = make_vector(7, (1, 2, 3, 4, 5, 6, 7))


def size(r):
    """
    return the size of the vector
    """
    return r(0)


def values(r):
    """
    return the values of the vector
    """
    return r(1)


def print_vector(v1):
    """
    print the vector's data
    """

    print("size = ", size(v1), "; values =", values(v1))


def value_at(v1, i):
    """
    return a value in the vector
    """

    return values(v1)[i]


def reverse(v1):
    """
    return  the revers of the vector
    """

    i = 0
    s = []
    while (i != size(v1)):
        s.append(values(v1)[size(v1) - i - 1])
        i += 1
    return make_vector(size(v1), tuple(s))


def norm1(v1):
    """
    return the vector's  sum of values in absolute
    """

    return sum(map(abs, values(v1)))


def norm2(v1):
    """
    return the vector's square of sum of values in power(2)
    """

    return (sum(map(lambda x: x ** 2, values(v1)))) ** 0.5


def insert(v1, nv):
    """
    add to the vector a new value
    """
    x = list(values(v1))
    x.append(nv)
    return make_vector(size(v1) + 1, tuple(x))


def delete(v1, indx):
    """
    delete a value in the victor in the index place
    """
    s = size(v1)
    if (size(v1) > indx):
        s -= 1
    x = list(values(v1))
    y = []
    for i in range(size(v1)):
        if i != indx:
            y.append(x[i])
    return make_vector(s, tuple(y))


def vector_sort(v1):
    """
    return a sorted vector
    """
    temp = list(values(v1))
    s = size(v1)
    for i in range(s):
        already_sorted = True
        for j in range(s - i - 1):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]

                already_sorted = False
        if already_sorted:
            break
    return make_vector(size(v1), tuple(temp))


def add_vector(v1, v2):
    """
    return a merge of two victor's
    """
    v1l = list(values(v1))
    v2l = list(values(v2))
    nv = tuple(v1l + v2l)
    return make_vector(size(v1) + size(v2), nv)


def mult_scalar(v1, val):
    """
    return the vector's values multiply with an enterd value
    """
    return make_vector(size(v1), tuple(map(lambda x: x * val, values(v1))))


###################################################################################################

# q3/1
def avg_grades(c1):
    """
    return the average of the courses
    """
    return tuple(map(second_avg, courses))


def second_avg(s):
    return (s[0], sum(s[1]) / len(s[1]))


courses = (('a', [81, 78, 57])), ('b', [95, 98]), ('c', [75, 45]), ('d', [58])
credits = (('b', 2.5), ('d', 4), ('c', 3.5), ('a', 5))

###################################################################################################


# q3/2

factors = (('c', 15), ('a', 20))


def sum_i(c, f):
    return c[0], c[1] + f[1]


def f(x):
    return x[0]


def c(c, f):
    if c[0] == f[0]:
        return (c[0], c[1] + f[1])
    else:
        return (c[0], c[1])


def add_factors(courses, factors):
    """
    update a course grade
    """
    factors = list(factors)
    factors.sort()

    factors = tuple(factors)

    split = tuple(map(lambda x: (tuple(filter(lambda y: y[0] == x[0], courses))), factors))

    split = tuple(map(f, split))

    courses = list(courses)
    split = list(split)

    sumt = tuple(map(sum_i, split, factors))

    return sumt


###################################################################################################

# q3/3
courses = (('a', [81, 78, 57])), ('b', [95, 98]), ('c', [75, 45]), ('d', [58])
credits = (('b', 2.5), ('d', 4), ('c', 3.5), ('a', 5))



def average_total(courses, credits):
    """
    return the general average of the courses
    """
    credits=sorted(credits)
    courses=sorted(courses)
    return sum(tuple(map(lambda x,y:x[1]*y[1], courses, credits))) / sum(tuple(map(lambda x: x[1], credits)))


#print(average_total(avg_grades(courses), credits))

###################################################################################################
# q4
courses = (('a', 80), ('b', 95), ('c', 75), ('d', 58))
credits = (('a', 2.5), ('b', 4), ('c', 3.5), ('d', 5))
courses_dict = dict(courses)
credits_dict = dict(credits)
types = {'t1': ('a', 'b'), 't2': ('c',), 't3': ('d',)}


def make_warehouse(courses_dict, credits_dict, types):
    """
    build new ware house with courses and its credits and type
    """

    def min_credits():
        """
        return the grade of the min credit
        """
        min_key = min(credits_dict, key=credits_dict.get)
        return courses_dict[min_key]

    def max_credits():
        """
        return the grade of the max credit
        """
        max_key = max(credits_dict, key=credits_dict.get)
        return courses_dict[max_key]

    def min_course(x):
        """
        return the min grade in the same type
        """
        indx = types[x]
        min_c = credits_dict[indx[len(indx) - 1]]
        for key in range(len(indx)):
            c = credits_dict[indx[key]]
            if min_c > c:
                min_c = c
            if credits_dict[indx[key]] == min_c:
                min_g = courses_dict[indx[key]]
        return min_g

    def max_course(x):
        """
         return the max grade in the same type
         """
        indx = types[x]
        max_c = 0
        for key in range(len(indx)):
            c = credits_dict[indx[key]]
            if max_c < c:
                max_c = c
            if credits_dict[indx[key]] == max_c:
                max_g = courses_dict[indx[key]]
        return max_g

    def avg_course(x):
        """
         return the average of a specific type
         """
        indx = types[x]
        sum = 0
        for key in range(len(indx)):
            sum += courses_dict[indx[key]]
        avg = sum / len(indx)
        return avg

    def add_course(course, grade, type):
        """
        add a new course and it's type and grade
         """

        indx = list(types[type])
        for key in range(len(indx)):
            indx.append(course)
        indx = tuple(indx)
        types[type] = indx
        newcourse = ((course, grade))
        global courses
        c = list(courses)
        c.append(newcourse)
        c = tuple(c)
        courses = c

    return {'min_credits': min_credits, 'max_credits': max_credits, 'min_course': min_course, 'max_course': max_course,
            'avg_course': avg_course, 'add_course': add_course}


w = make_warehouse(courses_dict, credits_dict, types)


###################################################################################################
# q5

def make_sequence(listx):
    """
     to use the the input as a sequence
    """

    def filter(func):
        """
         return the input as filtered tuple
         """
        if func == None:
            return tuple(listx)
        h_l = []
        for value in range(len(listx)):
            if func(listx[value]):
                h_l.append(listx[value])

        return tuple(h_l)

    def filter_iterator(func):
        """
         to get the next value or the previous one in a sequence
         """
        test_value = filter(func)
        indx = 0

        def next():
            nonlocal indx
            print(test_value[indx])
            indx = (indx + 1) % len(test_value)

        def reverse():
            nonlocal indx
            print(test_value[indx - 1])
            indx = (indx - 1) % len(test_value)

        return {'next': next, 'reverse': reverse}

    def reverse():
        """
         return the revers of the sequence
         """
        h_l = list(listx)
        new_lst = h_l[::-1]
        return new_lst

    def extend(add):
        """
         to add a new values to the sequence
         """
        nonlocal listx
        listx += tuple(add)

    return {'filter': filter, 'filter_iterator': filter_iterator, 'reverse': reverse, 'extend': extend}


s1 = make_sequence((1, 2, 3, 4, 5))
