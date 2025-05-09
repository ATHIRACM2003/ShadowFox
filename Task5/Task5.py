#Task 5: Classes and Objects

class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        print(f"\n\nName : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Super Power : {self.super_power}")
        print(f"Weapon : {self.weapon}")
        print(f"Leader : {'Yes' if self.is_leader() else 'No'}")

    def is_leader(self):
        return self.name == "Captain America"

super_heroes = [
    Avenger("Captain America", 105, "Male", "Super Strength", "Shield"),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows"),
]

for hero in super_heroes:
    hero.get_info()


    
