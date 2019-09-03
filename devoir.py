def menu():
    print("Matière:"
          " 1:Piano   "
          " 2:Ecole   "
          " 3:Anglais  ")
    choix_matiere = int(input("Quel Matière voulez vous utiliser: "))

    if(choix_matiere == 1):
        menu_piano()

    if(choix_matiere == 2):
        menu_ecole()

    if(choix_matiere == 3):
        menu_anglais()


def menu_piano():
    global devoirs_piano,date_devoirs_piano,compteur_devoirs

    print("1: Ajouter un nouveau devoir,  2: Voir les Devoirs, 3:Supprimer les devoirs  4:Revenir en arrière")
    choix_menu_piano = int(input("Que voulez vous faire ?"))
    if(choix_menu_piano == 1):
        devoirs_piano = str(input("Quels sont les devoirs?:  "))
        date_devoirs_piano = str(input("pour quand sont les devoirs?:  "))
        print("ok c'est bon")
        menu_piano()

    if(choix_menu_piano == 2):
        print("Voici les devoirs pour le :",date_devoirs_piano,"  ,",devoirs_piano)
        #fait_devoir = input("As-tu fait les devoirs")
        #if(fait_devoir == "o"):



        menu_piano()
    if(choix_menu_piano == 3):
        suppr_verification = input("Es tu sur de vouloirs supprimmer les devoirs (o/n)")
        if(suppr_verification == "o"):
            devoirs_piano = "Aucun devoirs"
            date_devoirs_piano = "-"
            print("Les devoirs ont été supprimés")
            menu_piano()
        else: menu_piano()


    if(choix_menu_piano == 4):
        menu()


if __name__ == '__main__':
    menu()
