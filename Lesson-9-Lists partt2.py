cars=['bmw','vw','seat','skoda','lada']

for x in cars:
    print(x.upper())

mynumber_list=list(range(0,10))
print(mynumber_list)

for x in mynumber_list:
    x=x*2
    print(x)
print(mynumber_list)

print(max(mynumber_list))
print(sum(mynumber_list))

mycars=cars[1:4]
print(mycars)

mycars=cars[:] #make a copy of array