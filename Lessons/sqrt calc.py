initial = int(input('Enter your number here:\t'))
x = 1
#while initial != x:
#    for i in range(1,initial+1):
#        x = i*i
#        print(x)
#else:
#    print('sqrt founded')

for i in range(1,initial+1):
    x=i*i
    if x == initial:
        print("sqrt is "+str(i))