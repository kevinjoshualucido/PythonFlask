class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 80
        self.energy = 50

    # methods
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 10
        return self

    def noise(self):
        print(self.noise)
        return self


class Ninja:
    # constructor and attributes
    def __init__(self, first_name, last_name, pet, treat, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treat = treat
        self.pet_food = pet_food

    # methods
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self


my_treats = ["bone", "sausage", "meat stick"]
my_pet_food = ["Badlands dog food", "Mr. Kibbles dog food"]
pet_tricks = ["sit", "circle", "shake hand"]

kookie = Pet("Kookie", "dog", pet_tricks, "whimper!")
josh = Ninja("Kevin Joshua", "Lucido", kookie, my_treats, my_pet_food)

josh.bathe()