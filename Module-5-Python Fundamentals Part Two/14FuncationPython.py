
# function defenations 
def hello ():
    print("hello world")

hello()


# parameter
def sum (a , b):
    s = a + b 
    return s 
result = sum(10 , 20 )
print(result)


# calc average 

def calc_average(a, b , c ):
    sum = a + b + c 
    return sum / 3

print(calc_average(5, 10, 15))