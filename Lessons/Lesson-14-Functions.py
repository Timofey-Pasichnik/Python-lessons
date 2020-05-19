def type_greeting(name):
    """Prints Greeting"""
    print('Congratulations, '+name+ ', wish you all the best!')
    print('How are you?')


def aaaa():
    print('AAAA')


def summa(x, y):
    return x+y


def factorial(x):
    otvet = 1
    for i in range(1, x+1):
        otvet = otvet * i
    return otvet


print('--------------------')
type_greeting('Denis')
type_greeting('Vasya')
aaaa()

x = summa(33, 22)
print(x)

print(factorial(5))