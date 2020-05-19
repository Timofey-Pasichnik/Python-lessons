enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'ogre',
    'awards': ['Killer', 'Slayer'],
    'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']
}

all_enemies = [enemy.copy(), enemy.copy(), enemy.copy(), enemy.copy()]

for x in range(0, 10):  # does the same
    all_enemies.append(enemy.copy())

for ene in all_enemies:
    print(ene)

all_enemies[5]['health']=30

for ene in all_enemies:
    print(ene)