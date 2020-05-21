import re

input_filename = "D:\DOC\Test files for Py\emails.txt"
result_filename = "D:\DOC\Test files for Py\l24results.txt"


inputfile = open(input_filename, mode='r', encoding='utf-8')
resultfile = open(result_filename, mode='w', encoding='utf-8')

print(inputfile)

lookfor = r"[\w\s.-]+@[\w.]+"

mytext = inputfile.read()

results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    resultfile.write(item+"\n")



print('Total: '+ str(len(results)))