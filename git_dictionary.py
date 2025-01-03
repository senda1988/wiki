def git_dictionary(befehl_git):
    git_dict = {
        "github": "ist eine Plattform für Versionskontrolle und Zusammenarbeit basierend auf Git.",
        "pull": "um Änderungen von einem entfernten Repository herunterzuladen und sie mit dem lokalen Repository zu vereinen.",
        "push": "die Änderungen von Ihrem lokalen Repository zu einem Remote-Repository (z. B. auf GitHub).",
        "clone": "entferntes Repository zu kopieren und es lokal zu speichern.",
        "commit": "Art Schnappschuss des aktuellen Zustands des Codes",
        "main-branch": "der Hauptzweig eines Projekts. Sie repräsentiert den stabilen und produktionsreifen Code.",
        "andere Branches": "Diese Branches dienen zur parallelen Entwicklung von Features, Behebung von Bugs oder Experimenten, ohne die Stabilität des Hauptcodes zu gefährden.",
        "merge": "um die Änderungen eines Branches in einen anderen zu integrieren.",
        "repository": "Ein Speicherort für Code und Dateien in Git. ",
    }
    if befehl_git.lower() in git_dict:
        print(f"der Befehle {befehl_git} wird verwendet {git_dict[befehl_git.lower()]}")
    else:
        print("dieser Befehle existiert nicht !!")
        neu_befehle = input(
            f"dieser Befehle existiert nicht. gib die beschreibung ein: "
        )
        git_dict[befehl_git] = neu_befehle
        print(f"Der befehle {befehl_git} : {git_dict[befehl_git]}")


befehla_input = input(" gib ein befehle ein: ").lower()
git_dictionary(befehla_input)
