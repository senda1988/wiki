class Zutat:
    def __init__(self, name, kalorien_pro_100g, zubereitungszeit):
        self.name = name
        self.kalorien_pro_100g = kalorien_pro_100g
        self.zubereitungszeit = zubereitungszeit


class Rezept(Zutat):

    def __init__(self, name, beschreibung, zutatenliste):
        self.name = name
        self.beschreibung = beschreibung
        self.zutatenliste = {}

    def zutat_hinzufugen(self, zutat, menge):
        self.zutatenliste[zutat] = menge

    def rezept_anzeigen(self):

        print(f"Rezept: {self.name}")
        print("Zutaten:")
        for zutat in self.zutatenliste:
            print(f" {zutat.name}: {self.zutatenliste[zutat]}")
        print(f"Beschreibung: {self.beschreibung}")

    def kalorien(self):
        kalor = 0
        for i in self.zutatenliste:
            kalor += i.kalorien_pro_100g / 100  # * self.menge
        print(f"zählt die Kalorien aller Zutaten in der zutatenliste: {kalor}")

    def kochzeit(self):
        i = 0
        zeit = 0
        for zutat in self.zutatenliste:
            if zutat.zubereitungszeit > zeit:
                zeit = zutat.zubereitungszeit
        print(
            f"die den höchsten Wert in ihrer zubereitungszeit hat: {zeit} de {zutat.name}"
        )


# Zutaten erstellen
lauwarmes_wasser = Zutat("lauwarmes Wasser", 0, 0)
hefe = Zutat("Hefe", 10, 0)
zucker = Zutat("Zucker", 1, 2)
ol = Zutat("Öl", 70, 0)
mehl = Zutat("Mehl", 300, 5)

rezept = Rezept(
    "Pizza",
    "Aus nur wenig Zutaten bekommt man einen leckeren Pizzateig, den man anschließend nach Belieben belegen kann. Die Zubereitung ist schnell und einfach.",
    {},
)
# Zutaten hinzufügen
rezept.zutat_hinzufugen(lauwarmes_wasser, "250 ml")
rezept.zutat_hinzufugen(hefe, "1 Würfel")
rezept.zutat_hinzufugen(zucker, "1 Prise")
rezept.zutat_hinzufugen(ol, "2 EL")
rezept.zutat_hinzufugen(mehl, "500 gr")
rezept.rezept_anzeigen()
rezept.kalorien()
rezept.kochzeit()
