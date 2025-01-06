# Aufgabe 1


text = input("Eingabe:")
buchstabe = input("Buchstabe:")
counter = 0

for i in range(len(text)):

    if buchstabe == text[i]:
        counter += 1
print(f"Der Buchstabe {buchstabe} kommt {counter}-mal vor")


# Aufgabe 2


sum = 0
for _ in range(5):
    var = int(input("Gib mir ein Zahl: "))
    sum += var
durchschnitt = sum / 5
print(f"Summe = {sum}, Durchschnitt = {durchschnitt}")


# Aufgabe 3
zahl = int(input("gibt die Anzahl der Zeilen ein: "))
i = 0
while i < zahl:
    i += 1
    print(i * "*")
