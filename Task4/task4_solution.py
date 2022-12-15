



#auther: osama khwaled



import datetime

'''
#q1
class Date(object):
""" date class : showing the date data"""
    def __init__(self,day=datetime.datetime.now().day,month=datetime.datetime.now().month,year=datetime.datetime.now().year):
        self.year=year
        self.month=month
        self.day=day

    def __str__(self):
        return str(self.day)+'/'+str(self.month)+'/'+str(self.year)

#d1=Date(1,2,2020)
#d2=Date()
#print(d1 ,'-',d2)

class Temperature(object):
""" the temprature class to provide info about it and date""" 
    def __init__(self,Temperature,day=datetime.datetime.now().day,month=datetime.datetime.now().month,year=datetime.datetime.now().year):
        self.year=year
        self.month=month
        self.day=day
        self.Temperature=Temperature
        return str(float(self.Temperature))+' °C'+':'+str(self.day)+'/'+str(self.month)+'/'+str(self.year)

    def __str__(self):

    def compareTemp(self,others):
        if self.Temperature>others.Temperature:
            return Temperature(self.Temperature)
        else:
            return Temperature(others.Temperature)

#t1=Temperature(-12,1,2,2020)
#t2=Temperature(0)
#t3=Temperature(32,20,8,2020)
#print(t1,',',t2,',',t3)
#print(t1.compareTemp(t3))


class Location(Temperature):
""" the Location class to provide info about the tempratrures in it and its date""" 

    def __init__(self,location,Temperature=None,list_temp=[]):
        self.location=location
        self.Temperature=Temperature.__init__()
        self.list_temp=list_temp
    def addTemp(self,Temp1=None,Temp2=None,Temp3=None,Temp4=None):
        self.list_temp.append(Temp1)
        self.list_temp.append(Temp2)
        self.list_temp.append(Temp3)
        self.list_temp.append(Temp4)

    def printLocation(self):# print the location data
        print(self.location)
        if self.list_temp== []:
            print("no temperature measurements available")
        else:
            for self.Temperature in self.list_temp:
                if self.Temperature!=None:
                    print(self.Temperature,' ',end='')
        print('\n')

    def getAverage(self):#get the the avg of the temp
        sum=0
        for self.Temperature in self.list_temp:
            sum+=self.Temperature.Temperature
        avg=sum/len(self.list_temp)

        return avg

    def getMaxTemp(self):   #get the max temp in a location
        max_temp=0

        for self.Temperature in self.list_temp:
            if max_temp<self.Temperature.Temperature:
                max_temp =self.Temperature.Temperature

        for self.Temperature in self.list_temp:
            if max_temp==self.Temperature.Temperature:
                chosen=self.Temperature
        return chosen

    def compareLocation(self,others):   # compare the temp between a different location
        if self.getAverage()>others.getAverage():
            return self
        else:
            return others





#loc1=Location('London')
#loc1.printLocation()
#loc1.addTemp(Temperature(9),Temperature(7,1,12,2020),Temperature(23,21,8,2020),Temperature(16,
#4,5,2020))
#print(loc1.getAverage())
#loc1.printLocation()
#loc2=Location('Berlin')
#loc2.addTemp(Temperature(6),Temperature(28,12,8,2020),Temperature(3,1,12,2020),Temperature(
#-3,2,1,2020))

#print('\n',loc1.getMaxTemp())
#(loc2.compareLocation(loc1)).printLocation()


########################################################################################################################
#q2
def make_class(attrs, base=None):
    """Return a new class (a dispatch dictionary) with given class attributes"""
    # Getter: class attribute (looks in this class, then base)
    def get(name):
        if name in attrs: return attrs[name]
        elif base:        return base['get'](name)
    # Setter: class attribute (always sets in this class)
    def set(name, value): attrs[name] = value
    # Return a new initialized object instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}
        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:       return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else:               return value
        # Setter: instance attribute (always sets in object)
        def set(name, value):       attrs[name] = value
        # instance dictionary
        obj = { 'get': get, 'set': set }
        # calls constructor if present
        init = get('__init__')
        if init: init(*args)
        return obj
    # class dictionary
    cls = { 'get': get, 'set': set, 'new': new }
    return cls

def make_date_class():
""" date class in shmython type: showing the date data"""

    def __init__(self,day=datetime.datetime.now().day,month=datetime.datetime.now().month,year=datetime.datetime.now().year):
        self['set']('year', year)
        self['set']('month', month)
        self['set']('day', day)

    def str(self):
        return '%02d/%02d/%02d'%(self['get']('day'), self['get']('month'), self['get']('year'))

    return make_class({'__init__':__init__,'str':str})


def  make_temperature_class():
""" the temprature class (shmython type) to provide info about it and date""" 

    def __init__(self,temperature,day=datetime.datetime.now().day,month=datetime.datetime.now().month,year=datetime.datetime.now().year):
        self['set']('year', year)
        self['set']('month', month)
        self['set']('day', day)
        self['set']('temperature',temperature)

    def str(self):
        return '%.1f°C:%02d/%02d/%02d'%(self['get']('temperature'),self['get']('day'), self['get']('month'), self['get']('year'))
    return make_class({'__init__':__init__,'str':str})

def make_location_class():
""" the Location class (shmython type) to provide info about the tempratrures in it and its date""" 

    def __init__(self, location, list_temp=[]):
        self['set']('location',location)
       # Temperature=make_temperature_class()
       # self['set']('temperature', temperature)
        self['set']('list_temp',list_temp)

    def printLocation(self):#print location shmython way
        print(self['get']('location'))
        if self['get']('list_temp')== []:
            print("no temperature measurements available")
        else:
            for i in range(len(self['get']('list_temp'))):
                print(self['get']('list_temp')[i]['get']('str')(),end=' ')
            print('\n')

    def addTemp(self,t1=None,t2=None,t3=None,t4=None):
        self['get']('list_temp').append(t1)
        self['get']('list_temp').append(t2)
        self['get']('list_temp').append(t3)
        self['get']('list_temp').append(t4)

    def getAverage(self):#get temp avg shmython way
        sum=0
        for i in range(len(self['get']('list_temp'))):
            sum+=self['get']('list_temp')[i]['get']('temperature')

        print(sum/len(self['get']('list_temp')))

    def getMaxTemp(self):
        max_temp=0
        for i in range(len(self['get']('list_temp'))):

            if max_temp<self['get']('list_temp')[i]['get']('temperature'):
                max_temp =self['get']('list_temp')[i]['get']('temperature')

        for i in range(len(self['get']('list_temp'))):
            if max_temp==self['get']('list_temp')[i]['get']('temperature'):
                chosen=self['get']('list_temp')[i]
        return chosen


    def compareLocation(self,others):
        if self['get']('getAverage')()>others['get']('getAverage')():
            return self
        else:
            return others

    return make_class({'__init__': __init__, 'printLocation': printLocation,'addTemp':addTemp,'getAverage':getAverage,'getMaxTemp':getMaxTemp,'compareLocation':compareLocation})

Date=make_date_class()
d1=Date['new'](1,2,2020)
d2=Date['new']()
#print(d1['get']('str')(),'-',d2['get']('str')())

#Temperature = make_temperature_class()
#t1=Temperature['new'](-12,1,2,2020)
#t2=Temperature['new'](0)
#t3=Temperature['new'](32,20,8,2020)
#print(t1['get']('str')(),',',t2['get']('str')(),',',t3['get']('str')())

#Location=make_location_class()
#loc1 = Location['new']('London')
#loc1['get']('printLocation')()
#loc1['get']('addTemp')(Temperature['new'](9),Temperature['new'](7,1,12,2020),Temperature['new'](23,21,8,2020),Temperature['new'](16,4,5,2020))
#loc1['get']('printLocation')()
#loc1['get']('getAverage')()
#print(loc1['get']('getMaxTemp')()['get']('str')())


########################################################################################################################
#q3# add to make_class name_S argument and path fo the father base
def make_class(name_s,attrs,base=None):
    """Return a new class (a dispatch dictionary) with given class attributes"""
    # Getter: class attribute (looks in this class, then base)
    def get(name):
        if name in attrs: return attrs[name]
        elif base:        return base['get'](name)
    # Setter: class attribute (always sets in this class)
    def set(name, value):
        attrs[name] = value

    # Return a new initialized object instance (a dispatch dicti  m   monary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}
        name_s=''
        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:       return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else:               return value
        # Setter: instance attribute (always sets in object)
        def set(name, value):       attrs[name] = value
        # instance dictionary
        obj = { 'get': get, 'set': set }
        # calls constructor if present
        init = get('__init__')
        if init: init(*args)
        return obj

    def class_path():
        if base:
            print(base['get']('name'),'::',name_s)
        else:
            print(get('name'))

    # class dictionary
    set('class_path', base)
    cls = { 'get': get, 'set': set, 'new': new,'class_path':class_path}
    set('name', name_s)



    return cls

def make_account_class():
    return make_class('Account', {'interest' : 0.05})
def make_save_account_class():
     def init(self, owner):
        self['set']('owner',owner)
        self['set']('balance',0)
     return make_class('SaveAccount', {'__init__' : init, 'interest' : 0.03}, Account)
Account = make_account_class()
SaveAccount = make_save_account_class()
print(Account['get']('name'))
print(SaveAccount['get']('name'))
Account['class_path']()
SaveAccount['class_path']()

########################################################################################################################
#q4/5
from fractions import gcd
from math import atan2, sin, cos, pi


####################
# Rational numbers #
####################

def add_Exponential(x, y):
    """Add Exponential numbers x and y."""

    if x.pow>y.pow:
        p=y.pow
    else:
        p=x.pow

    res=(x.ten*x.base+y.ten*y.base)/10**p
    return repr(Exponential(res, p))


def mul_Exponential(x, y):
    """Multiply Exponential numbers x and y."""
    return repr(Exponential(x.base * y.base, x.pow + y.pow))


class Exponential(object):
    """A Exponential number represented as a base number and the power value."""

    def __init__(self, base, pow,ten=10):
        self.base = base
        self.pow = pow
        self.ten=ten**pow
    def __repr__(self):
        return 'Exponential({0}, {1})'.format(self.base, self.pow)

    def __str__(self):
        return '{0}/{1}'.format(self.base, self.pow)


##########################################################################
def add_rational(x, y):
    """Add rational numbers x and y."""
    nx, dx = x.numer, x.denom
    ny, dy = y.numer, y.denom
    return Rational(nx * dy + ny * dx, dx * dy)


def mul_rational(x, y):
    """Multiply rational numbers x and y."""
    return Rational(x.numer * y.numer, x.denom * y.denom)


class Rational(object):
    """A rational number represented as a numerator and denominator."""

    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)


###################
# Complex numbers #
###################

def add_complex(z1, z2):
    """Return a complex number z1 + z2"""
    return ComplexRI(z1.real + z2.real, z1.imag + z2.imag)


def mul_complex(z1, z2):
    """Return a complex number z1 * z2"""
    return ComplexMA(z1.magnitude * z2.magnitude, z1.angle + z2.angle)


class ComplexRI(object):
    """A rectangular representation of a complex number.

    >>> from math import pi
    >>> add_complex(ComplexRI(1, 2), ComplexMA(2, pi/2))
    ComplexRI(1.0000000000000002, 4.0)
    >>> mul_complex(ComplexRI(0, 1), ComplexRI(0, 1))
    ComplexMA(1.0, 3.141592653589793)
    """

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    def __repr__(self):
        return 'ComplexRI({0}, {1})'.format(self.real, self.imag)


class ComplexMA(object):
    """A polar representation of a complex number."""

    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return 'ComplexMA({0}, {1})'.format(self.magnitude, self.angle)


##############################
# Tag-based type dispatching #
##############################

def type_tag(x):
    """Return the tag associated with the type of x."""
    return type_tag.tags[type(x)]


type_tag.tags = {ComplexRI: 'com', ComplexMA: 'com', Rational: 'rat', Exponential: 'Exp'}


def add(z1, z2):
    """Add z1 and z2, which may be complex or rational.

    >>> add(ComplexRI(1.5, 0), Rational(3, 2))
    ComplexRI(3.0, 0)
    >>> add(Rational(5, 3), Rational(1, 2))
    Rational(13, 6)
    """
    types = (type_tag(z1), type_tag(z2))
    return add.implementations[types](z1, z2)

########################################################################################################################
#q4f
def add_Exponential_and_rational(z, r):#add rat num to exp num
    return repr(Exponential(((z.base * z.ten) + (r.numer / r.denom)) / z.ten, z.pow))


add_rational_and_Exponential = lambda r, z: add_Exponential_and_rational(z, r)#

def or_Exponential_or_complexRI(z, r):#add exp value to complixRI values
    return  repr(ComplexRI(((z.base * z.ten) + r.real),r.imag))


def mul_Exponential_and_complexMA(z, r):
    return  repr(ComplexMA(((z.base * z.ten) ),r.angle))


def mul_Exponential_and_rational(z, r):
    return repr(Rational(((z.base * z.ten) * (r.numer / r.denom))**-1 *((z.base * z.ten) * (r.numer / r.denom)) , ((z.base * z.ten) * (r.numer / r.denom))**-1))


########################################################################################################################
def add_Exponential_and_rational_2_compRI(z, r):#
    return repr(ComplexRI(((z.base * z.ten) + (r.numer / r.denom)) , 0))

#def or_Exponential_or_complexRI(z, r):#
 #   return  repr(ComplexRI(((z.base * z.ten) + r.real),r.imag))

def add_Exponential_2_compRI(x, y):
    """Add Exponential numbers x and y and convert to complixRI."""
    res=(x.ten*x.base+y.ten*y.base)
    return repr(ComplexRI(res, 0))

def mul_Exponential_2_compMA(x, y):
    """Multiply Exponential numbers x and y."""
    zero:float=0
    return repr(ComplexMA((x.base *x.ten)* (y.base*y.ten), zero))

def mul_Exponential_and_complexRI_2_compMA(z, r):
    return  repr(ComplexMA(((z.base * z.ten) ),r.angle))

########################################################################################################################
def add_complex_and_rational(z, r):
    return ComplexRI(z.real + float(r.numer) / r.denom, z.imag)


add_rational_and_complex = lambda r, z: add_complex_and_rational(z, r)

add.implementations = {}

add.implementations[('Exp', 'Exp')] = add_Exponential_2_compRI
add.implementations[('Exp', 'Exp')] = mul_Exponential_2_compMA
add.implementations[('Exp', 'com')] = or_Exponential_or_complexRI

add.implementations[('Exp', 'rat')] = add_Exponential_and_rational_2_compRI
add.implementations[('Exp', 'com')] =mul_Exponential_and_complexRI_2_compMA
add.implementations[('Exp', 'com')] = mul_Exponential_and_complexMA
add.implementations[('Exp', 'rat')] = mul_Exponential_and_rational


############
# Coercion #
############

def rational_to_complex(x):
    return ComplexRI(x.numer / x.denom, 0)


coercions = {('rat', 'com'): rational_to_complex,('Exp', 'Exp'):add_Exponential_2_compRI,('Exp', 'Exp'):mul_Exponential_2_compMA,('Exp', 'com'): or_Exponential_or_complexRI
             ,('Exp', 'rat'): add_Exponential_and_rational_2_compRI,('Exp', 'com'):mul_Exponential_and_complexRI_2_compMA,('Exp', 'com'):mul_Exponential_and_complexMA,('Exp', 'rat'): mul_Exponential_and_rational}


def coerce_apply(operator_name, x, y):
    """Apply an operation ('add' or 'mul') to x and y.

    >>> coerce_apply('add', ComplexRI(1.5, 0), Rational(3, 2))
    ComplexRI(3.0, 0)
    >>> coerce_apply('mul', Rational(1, 2), ComplexMA(10, 1))
    ComplexMA(5.0, 1.0)
    """
    tx, ty = type_tag(x), type_tag(y)
    if tx != ty:
        if (tx, ty) in coercions:
            tx, x = ty, coercions[(tx, ty)](x)
        elif (ty, tx) in coercions:
            ty, y = tx, coercions[(ty, tx)](y)
        else:
            return 'No coercion possible.'
    assert tx == ty
    key = (operator_name, tx)
    return coerce_apply.implementations[key](x, y)


coerce_apply.implementations = {('mul', 'com'): mul_complex,
                                ('mul', 'rat'): mul_rational,
                                ('add', 'com'): add_complex,
                                ('add', 'rat'): add_rational,
                                ('add', 'com'): add_Exponential_2_compRI,
                                ('mul', 'com'): mul_Exponential_2_compMA,
                                ('add', 'com'): or_Exponential_or_complexRI,
                                ('add', 'com'): add_Exponential_and_rational_2_compRI,
                                ('mul', 'com'): mul_Exponential_and_complexRI_2_compMA,
                                ('mul', 'com'): mul_Exponential_and_complexMA,
                                ('mul', 'com'): mul_Exponential_and_rational
}

def isExponential(v):
    return type(v)==Exponential
def isRational(v):
    return type(v)==Rational
def isComplexRI(v):
    return type(v)==ComplexRI
def isComplexMA(v):
    return type(v)==ComplexMA

def apply(operator_name, x, y):# apply function to  make a path for an operation to function
    if operator_name=='add':
        if isExponential(x) and isRational(y):
            return add_Exponential_and_rational(x,y)
        if isExponential(x) and isComplexRI(y):
            return or_Exponential_or_complexRI(x,y)
        if isExponential(x) and isExponential(y):
            return add_Exponential(x,y)
    if operator_name=='mul':
        if isExponential(x) and isExponential(y):
            return mul_Exponential(x,y)
        if isExponential(x) and isComplexMA(y):
            return mul_Exponential_and_complexMA(x,y)
        if isExponential(x) and isRational(y):
            return mul_Exponential_and_rational(x,y)


    return apply.implementations[key](x, y)


########################################################################################################################
#6
def make_sequence(listx=None):
    """
     to use the the input as a sequence
    """
    if type(listx) != tuple :if the seques hasnt been taken or not tuple run exception
        try:
            raise TypeError
        except TypeError:
            print("<class 'TypeError'> : no sequence argument")

    def filter(func=None):

#if the value of func is none run an exeption
        try:
            if func == None:
                raise TypeError
        except TypeError:
                print("<class 'TypeError'> : No filter function")

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

    def filter_iterator(func=None):
        try:#if the value of func is none run an exeption
            if func == None:
                 raise TypeError
        except TypeError:
                print("<class 'TypeError'> : No filter function")
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


# s1 = make_sequence()
# s1 = make_sequence(200)
s1 = make_sequence((1, 2, 3, 4, 5))
#s1['filter']()
p1=s1['filter_iterator']()


# s1 = make_sequence((1, 2, 3, 4, 5))
# p1=s1['filter_iterator'](lambda x: x<4)
# p1['next']()

#######################################################################################################################
#8
"""Calculator

An interpreter for a calculator language using prefix-order call syntax.
Operator expressions must be simple operator names or symbols.  Operand
expressions are separated by commas.

Examples:
    calc> mul(1, 2, 3)
    6
    calc> add()
    0
    calc> add(2, div(4, 8))
    2.5
    calc> add
    SyntaxError: expected ( after add
    calc> div(5)
    TypeError: div requires exactly 2 arguments
    calc> div(1, 0)
    ZeroDivisionError: division by zero
    calc> ^DCalculation completed.
"""

from functools import reduce
from operator import mul, add


def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc. <ctrl-C>
            print('Calculation completed.')
            return


# Eval & Apply

class Exp(object):
    """A call expression in Calculator.

    >>> Exp('add', [1, 2])
    Exp('add', [1, 2])
    >>> str(Exp('add', [1, Exp('mul', [2, 3])]))
    'add(1, mul(2, 3))'
    """

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)


def calc_eval(exp):
    """Evaluate a Calculator expression.

    >>> calc_eval(Exp('add', [2, Exp('mul', [4, 6])]))
    26
    """
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)


def calc_apply(operator, args):
    """Apply the named operator to a list of args.

    >>> calc_apply('+', [1, 2, 3])
    6
    >>> calc_apply('-', [10, 1, 2, 3])
    4
    >>> calc_apply('*', [])
    1
    >>> calc_apply('/', [40, 5])
    8.0
    """
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer / denom


# Parsing

def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree


def tokenize(line):
    """Convert a string into a list of tokens.

    >>> tokenize('add(2, mul(4, 6))')
    ['add', '(', '2', ',', 'mul', '(', '4', ',', '6', ')', ')']
    """
    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    return spaced.strip().split()


known_operators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/']


def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens.

    Operand expressions can be separated by commas, spaces, or both.

    >>> analyze(tokenize('add(2, mul(4, 6))'))
    Exp('add', [2, Exp('mul', [4, 6])])
    >>> analyze(tokenize('mul(add(2, mul(4, 6)), add(3, 5))'))
    Exp('mul', [Exp('add', [2, Exp('mul', [4, 6])]), Exp('add', [3, 5])])
    """
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
        raise SyntaxError('unexpected ' + token)


def analyze_operands(tokens):
    """Analyze a sequence of comma-separated operands."""
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)  # Remove )
    return operands


def assert_non_empty(tokens):
    """Raise an exception if tokens is empty."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')


def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token.

    >>> analyze_token('12')
    12
    >>> analyze_token('7.5')
    7.5
    >>> analyze_token('add')
    'add'
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token


def run():
    read_eval_print_loop()


run()
'''