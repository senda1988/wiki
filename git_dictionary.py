def git_dictionary(befehl_git):
    git_dict = {
        "GitHub": "Eine Plattform für Versionskontrolle und Zusammenarbeit, die auf Git basiert.",
        "pull": "Lädt Änderungen von einem entfernten Repository herunter und vereint sie mit dem lokalen Repository.",
        "push": "Überträgt Änderungen von Ihrem lokalen Repository in ein entferntes Repository (z. B. auf GitHub).",
        "clone": "Erstellt eine Kopie eines entfernten Repositorys und speichert sie lokal.",
        "commit": "Ein Schnappschuss des aktuellen Zustands des Codes mit einer Beschreibung der Änderungen.",
        "main-branch": "Der Hauptzweig eines Projekts, der den stabilen und produktionsreifen Code repräsentiert.",
        "andere Branches": "Branches, die zur parallelen Entwicklung von Features, Bugfixes oder Experimenten dienen, ohne die Stabilität des Hauptcodes zu gefährden.",
        "merge": "Integriert die Änderungen eines Branches in einen anderen.",
        "repository": "Ein Speicherort für Code, Dateien und die Git-Historie.",
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
