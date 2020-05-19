#name = input('Please enter your name: ')
#num1 = input('Hello, '+name+'! Enter first number, please\n')
#num2 = input('Great! Now enter a second number\n')
#total_sum = int(num1) + int(num2)
#print('The result of adding is '+str(total_sum))

#print(name+', you are using unregistered version of program. Enter a registration code below')
#code = '0'
#while code != 'FS654DY':
#    code = input()
#    print('Authentication failed!')
#print('Thanks for registering program. Welcome aboard, '+name+'!')

mylist = []
msg=''
while msg != 'stop':
    msg = input('Enter new item, type "stop" to finish')
    mylist.append(msg)
print('done, your array is '+ str(mylist))