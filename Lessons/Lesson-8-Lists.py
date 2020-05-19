cities=['new york','moscow','New Deli','Atlanta','pasadena']
print(cities)
print(len(cities))
print(cities[0]) # array starts from 0
print(cities[-1]) # print first from the end
print(cities[3].upper())
cities[2]='tula'
print(cities[2])
cities.append('Kurst') # add element of array in the end
print(cities)
cities.insert(3,'Novosibirsk') #add element at the number of array
print(cities)

del cities[-1] # delete first from the end in array
print(cities)

cities.remove('tula') #delete element "Tula"
print(cities)

deleted_city=cities.pop() #delete last element of array "cities" and write it to variable deleted_city

print(deleted_city)
print(cities)

cities.sort() #sorts array
print(cities)

cities.sort(reverse=true) #sorts array
print(cities)

for x in range(0,100):
    ramnod[x]=x
print(len(ramnod))