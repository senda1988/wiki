# gerichte = []
# for _ in range(3):
#     libling_gericht = input("gib dein liblinggericht: ")
#     gerichte.append(libling_gericht)

# for i in gerichte:
#     print(f"dein {gerichte.index(i)} gericht ist : {i}")
#     # print(f"dein liblingsgericht: {i}")


# weekdays = ["Montag", "Dienstag", "Mittwoch"]
# food = []
# for w in weekdays:
#     for i in range(2):
#         food_input = input(f"{i} - Was möchtest du am {w} essen?")
#         food.append(food_input)
# print(f"Der Essensplan für die gesamte Woche sieht wie folgt aus: {food}")


class Mathe:
    def addieren(self, x, y):
        return x + y


mathe_objekt = Mathe()
print(mathe_objekt.addieren(5, 3))
