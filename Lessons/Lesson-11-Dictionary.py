#   *****[ITEM]*****
#   *[KEY]**[VALUE]*
enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'ogre',
}

print(enemy)
print('Detected ' + str(enemy['name']) + ' at ' + str(enemy['loc_x']) + 'x ' + str(enemy['loc_y']) + 'y!')

enemy['rank'] = 'admiral'
print(enemy)

del enemy['rank']
print(enemy)

enemy['loc_x']=enemy['loc_x']+40
enemy['health']=enemy['health']-30
if enemy['health']<80:
    enemy['color']='yellow'
print(str(enemy['loc_x'])+' and color is '+enemy['color'])

print(enemy.keys())
print(enemy.values())
print(enemy)
