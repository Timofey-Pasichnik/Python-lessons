#inputfile = "D:/DOC/Test files for Py/names.txt"

#myfile = open(inputfile, mode='r', encoding='ascii') #1- path to file 2- mode r-read w- write - a- append, r+ read and write

#print(myfile.read()) open whole file. Can show error during decode. in this case use another encoding, e.g. utf-8

#for num, line in enumerate(myfile, 1): #line goes to myfile, but num goes to enumerate
#    if 'Mackie' in line:
#        print('Line № '+str(num)+':'+line.strip())
inputfile = "D:/DOC/Test files for Py/passwords.txt"
outputfile = "D:/DOC/Test files for Py/mypasswords.txt"

password_tolookfor = '123'

myfile = open(inputfile, mode='r', encoding='utf-8')
myfile2 = open(outputfile, mode='w', encoding='utf-8')

for num, line in enumerate(myfile, 1):
    if password_tolookfor in line:
        print('Line № '+str(num)+':'+line.strip())
        myfile2.write('Found password: '+line)

myfile.close()
myfile2.close()