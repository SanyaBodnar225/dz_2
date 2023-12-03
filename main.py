import random

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.energy = 100
        self.hunger = 0

    def sleep(self, hours):
        print(f"{self.name} спала {hours} годин.")
        self.energy += hours * 10
        if self.energy > 100:
            self.energy = 100

    def play(self, minutes):
        print(f"{self.name} грається {minutes} хвилин.")
        self.energy -= minutes * 2
        if self.energy < 0:
            self.energy = 0
        self.hunger += minutes * 1
        if self.hunger > 100:
            self.hunger = 100

    def eat(self, amount):
        print(f"{self.name} поїла.")
        self.hunger -= amount
        if self.hunger < 0:
            self.hunger = 0

    def status(self):
        print(f"{self.name} має енергія: {self.energy}, голод: {self.hunger}")

cat1 = Cat("Муся", "gray")
cat1.status()

cat1.play(30)
cat1.status()

cat1.eat(20)
cat1.status()

cat1.sleep(5)
cat1.status()