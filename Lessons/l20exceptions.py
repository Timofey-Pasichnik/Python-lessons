import sys

filename ="lesson_list.txt"

while True:
    try:
        print('inside TRY')
        myfile = open(filename, mode='r', encoding='utf-8')
    except Exception:
        print('inside EXCEPT')
        print('Error found')
        print(sys.exc_info()[1])
        #sys.exit() #break the program
        filename = input('Enter correct file name: ')
    else:
        print('inside ELSE')
        print(myfile.read())
        sys.exit()

print('inside FINALLY')
