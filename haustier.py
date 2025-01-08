class Haustier:
    def __init__(self, name, species, age, favorite_food):
        self.name = name
        self.species = species
        self.age = age
        self.favorite_food = favorite_food
        self.energy_level = 100

    def get_description(self):
        return f"{self.name} ist ein {self.age} Jahre alter {self.species}."

    def play(self, duration):

        if self.energy_level > 0:
            self.energy_level = self.energy_level - (duration * 5)
        else:
            self.energy_level = 0
        return self.energy_level

    def feed(self, food):

        if food == self.favorite_food:
            self.energy_level += 30
        else:
            self.energy_level += 10

        if self.energy_level > 100:
            self.energy_level -= self.energy_level - 100
        return self.energy_level

    # Bonus
    def sleep(self, hours):

        self.energy_level += 20 * hours
        if self.energy_level > 100:
            self.energy_level -= self.energy_level - 100
        return self.energy_level


katze = Haustier("Mimi", "katze", 3, "Fisch")
print(f"{katze.get_description()}")
# Mimi hat 15 Minuten gespielt und hat jetzt 25% Energie.
print(f"{katze.name} hat 15 Minuten gespielt und hat jetzt {katze.play(15)}% Energie")
print(
    f"{katze.name} liebt {katze.favorite_food}! Die Energie ist jetzt {katze.feed(katze.favorite_food)} %"
)

food = "Trockenfutter"
print(
    f"{katze.name} hat  Trockenfutter gegessen. Die Energie ist jetzt {katze.feed(food)} %"
)
hours_sleep = 2
print(
    f"{katze.name} hat  {hours_sleep} schlöft. Die Energie ist jetzt {katze.sleep(hours_sleep)} %"
)

hund = Haustier("BOBI", "Hund", 5, " Fleisch")

print(f"{hund.get_description()}")
print(f"{hund.name} hat 10 Minuten gespielt und hat jetzt {hund.play(10)}% Energie")
print(
    f"{hund.name} liebt {hund.favorite_food}! Die Energie ist jetzt {hund.feed(hund.favorite_food)} %"
)

food = "Trockenfutter"
print(
    f"{hund.name} hat  Trockenfutter gegessen. Die Energie ist jetzt {hund.feed(food)} %"
)
hours_sleep = 2
print(
    f"{hund.name} hat  {hours_sleep} hours geschlaffen. Die Energie ist jetzt {hund.sleep(hours_sleep)} %"
)
