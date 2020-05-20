import json
filename = "D:/DOC/Test files for Py/user_settings.txt"
myfile = open(filename, mode='w', encoding='utf-8')

player1 = {
    'PlayerName': 'Scott Wimbey',
    'Score': 58,
    'awards': ['TRE','GDJ','FML']
}

player2 = {
    'PlayerName': 'Derr Suite',
    'Score': 68,
    'awards': ['SMB','CTS','LYR']
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

json.dump(myplayers, myfile)
myfile.close()


myfile = open(filename, mode='r', encoding='utf-8')
json_data = json.load(myfile)

for user in json_data:
    print('player name is: '+ str(user['PlayerName']))
    print('player score is: '+ str(user['Score']))
    print('player awards are:' +str(user['awards']))