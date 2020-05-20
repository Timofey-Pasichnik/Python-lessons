class Main_unit():
    def __init__(self, name, level, race):
        """Initiate of parametres"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100


    def show_hero(self):
        """Print all values of unit"""
        description = (self.name + "'s level is:" + str(self.level) + "\n" + "He has " + str(self.health) + " HP\n").title()
        print(description)

    def level_up(self):
        self.level += 1
        self.health += 20
    def move(self):
        print("Unit " + self.name + " starts to move")


class Superhero(Main_unit):
    def __init__(self, name, level, race, magiclevel):
        super().__init__(name, level,race)
        self.magiclevel = magiclevel
        self.magic = int(100)

    def makemagic(self):
        self.magic -= 10

    def show_hero(self):
        description = (self.name + "'s level is:" + str(self.level) + "\n" + "He has " + str(
            self.health) + " HP\n" + "magic = " + str(self.magic)).title()
        print(description)