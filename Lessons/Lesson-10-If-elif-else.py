x=25
if x==23:
    print('YES you are right')
else:
    print('NO, you are wrong')
print('----------------------------')
age=2
if age<=4:
    print('You are baby')
elif age>4 and age<12:
    print('You are kid')
elif age>=12 and age<19:
    print('You are teenager')
else:
    print('You are old')
print('----------------------------')
all_cars=['chrysler','dacia','bmw','KIA','vw','seat','skoda','lada','audi','ford','Chevrolett']
german_cars=['bmw,','vw','audi']

for x in all_cars:#first method of find
    if x=='lada':
        print('yep,lada is here')
    else:
        print('its not a lada')
print('----------------------------')
if 'lada' in all_cars:
    print('lada is here')
else:
    print('lada is absent today')
print('----------------------------')

for x in all_cars:
    if str(x) in german_cars:
        print(str(x)+' is a german car')
    else:
        print(str(x)+' is not a german car')