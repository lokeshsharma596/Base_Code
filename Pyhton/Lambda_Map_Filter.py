# Lambda Function
# any no of arguments but only one statement
# single line ,anoymous,no def,no return

# example-1

def sum(a, b, c): return a+b+c

print(sum(4, 5, 1))


add=lambda a,b,c: a+b+c
print(add(4, 5, 1))

# example-2


cube=lambda n:n**3

print(cube(4))

# Map Function
# Atleast Two arguments :function and an iterable
# Iterable(list,string,dictionary,set,tuple)
# runs the lambda for each value in iterable and return a map object which,
# can be converted into any data structure

# example-1
nums = [1, 2, 3, 4, 5]


def sq(n):
    return n*n


square = list(map(sq, nums))
print(square)

# example-2
nums = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**x, nums))
print(square)

# example-3
people = ["lokesh", "sharma", "python", "developer"]
up = list(map(lambda x: x.upper(), people))
print(up)

# example-4
names = [
    {'first': 'lokesh', 'last': 'sharma'},
    {'first': 'ravi', 'last': 'sharma'},
    {'first': 'jiu', 'last': 'sharma'}
]
first_names = list(map(lambda x: x['first'], names))
print(first_names)


# Filter
# There is a lambda for each value in iterable
# return only values which are true to lambda

# example-1

names = ['anthony', 'penny', 'austing', 'boy', 'amio']
a = list(filter(lambda x: x[0] == 'a', names))
print(a)

# example-2
#filter inactive users

users = [
    {"username": 'samuel', "tweets": ["i love cake", "i am good"]},
    {"username": 'andy', "tweets": []},
    {"username": 'kumal', "tweets": ["India", "Python"]},
    {"username": 'sam', "tweets": []},
    {"username": 'lokesh', "tweets": ["i am good"]},
]

inactive_users = list(filter(lambda a:not a['tweets'], users))
print(inactive_users)


#example-3
#filter inactive users with just username in uppercase
inactive_users=list(map(lambda x: x["username"].upper(),
filter(lambda a:not a['tweets'], users)))
print(inactive_users)


#example-4
#return a new list with the string "your name is" + name 
# but only if length of name is less than five

names=['lokesh','lassie','bob','to']
new=list(map(lambda name:f"your name is {name}",
        filter(lambda x:len(x)>4,names)))
print(new)


#List Comprehension
# for example 2
inactive_users=[user for user in users if not user["tweets"]]
print(inactive_users)
# for example 3
inactive_users=[user["username"].upper() for user in users if not user["tweets"]]
print(inactive_users)