def git_dictionary(befehle_git):
    git_dict = {
        "pull": "um Änderungen von einem entfernten Repository herunterzuladen und sie mit dem lokalen Repository zu vereinen.",
        "push": " um Änderungen aus dem lokalen Repository in ein entferntes Repository zu übertragen.",
        "clone": " um ein entferntes Repository zu kopieren und es lokal zu speichern.",
        "commit": " um Änderungen im lokalen Repository zu speichern, zusammen mit einer Nachricht, die die Änderungen beschreibt.",
        "branch": "um alle Branches im Repository aufzulisten oder einen neuen Branch zu erstellen.",
        "merge": "um die Änderungen eines Branches in einen anderen zu integrieren.",
    }
    if befehle_git.lower() in git_dict:
        print(
            f"der Befehle {befehle_git} wird verwendet {git_dict[befehle_git.lower()]}"
        )
    else:
        print("dieser Befehle existiert nicht !!")
        neu_befehle = input(
            f"dieser Befehle existiert nicht. gib die beschreibung ein: "
        )
        git_dict[befehle_git] = neu_befehle
        print(f"Der befehle {befehle_git} wird verwendet, {git_dict[befehle_git]}")


befehla_input = input(" gib ein befehle ein: ").lower()
git_dictionary(befehla_input)
