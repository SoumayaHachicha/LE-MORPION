from random import randint

tableau = []
coordonnee_ligne = 2
coordonnee_colonne = 2

def initialise_game(tableau):
    '''for i in range(3):
        lst = ["-"]
        for j in range(2):
            lst.append("-")
            print(tableau[i][j], end="")
        print()
        tableau.append(lst)'''
    for i in range(3):
        lst = []
        for j in range(3):
            lst.append("#")
        tableau.append(lst)


def show_play():
    '''initialise_game(tableau)
    for i in range(3):
        for j in range(2):
            print(tableau, end="")
        print()'''
    '''for i in range(3):
        lst = ["-"]
        for j in range(2):
            lst.append("-")
        print(lst)'''
    for i in range(3):
        for j in range(3):
            print(tableau[i][j], end="")
        print()


def choose_ia_play():
    global IA
    if player == "X":
        print("L'ordinateur va jouer avec le O")
        IA = "O"

    else:
        print("L'ordinateur va jouer avec le X")
        IA = "X"


#def case_aleatoir(case_aleatoir_colonne, case_aleatoir_ligne):
    #case_aleatoir_colonne = randint(0, 2)
    #case_aleatoir_ligne = randint(0, 2)

def place_ia(coordonnee_colonne, coordonnee_ligne):
    choose_ia_play()
    initialise_game(tableau)
    case_aleatoir_colonne = randint(0, 2)
    case_aleatoir_ligne = randint(0, 2)
    #case_aleatoir(case_aleatoir_colonne, case_aleatoir_ligne)
    if tableau[case_aleatoir_ligne][case_aleatoir_colonne] != tableau[coordonnee_ligne][coordonnee_colonne] == player:
        tableau[case_aleatoir_ligne][case_aleatoir_colonne] = IA
    else:
        place_ia(coordonnee_colonne, coordonnee_ligne)

def util_player():
    global player
    player = input("Veuillez saisir votre joueur, soit 'X' soit 'O':")
    if player == "X":
        player = "X"
        print("Vous avez choisit: 'X'")

    elif player == "O":
        player = "O"
        print("Vous avez choisit: 'O'")

    else:
        print("ERROR!")
        util_player()

def depart_player():
    initialise_game(tableau)
    tableau[2][2] = player
    show_play()
    #return coordonnee_ligne

def choix_or_valid():
    global choix
    choix = input("Veuillez saisir (y) ou (n)")

def move_player_before_chooce(coordonnee_ligne, coordonnee_colonne):
    show_play()
    while choix != "y":
        bouton = int(input("Veuillez saisir:(8(haut),6(droite),4(gauche),2(bas):"))
        if bouton == 8 and coordonnee_ligne > 0:
            initialise_game(tableau)
            tableau[coordonnee_ligne-1][coordonnee_colonne] = player
            tableau[coordonnee_ligne][coordonnee_colonne] = "#"
            coordonnee_ligne -= 1
            show_play()

        elif bouton == 6 and coordonnee_colonne < 2:
            initialise_game(tableau)
            tableau[coordonnee_ligne][coordonnee_colonne+1] = player
            tableau[coordonnee_ligne][coordonnee_colonne] = "#"
            coordonnee_colonne += 1
            show_play()

        elif bouton == 4 and coordonnee_colonne > 0:
            initialise_game(tableau)
            tableau[coordonnee_ligne][coordonnee_colonne-1] = player
            tableau[coordonnee_ligne][coordonnee_colonne] = "#"
            coordonnee_colonne -= 1
            show_play()

        elif bouton == 2 and coordonnee_ligne < 2:
            initialise_game(tableau)
            tableau[coordonnee_ligne+1][coordonnee_colonne] = player
            tableau[coordonnee_ligne][coordonnee_colonne] = "#"
            coordonnee_ligne += 1
            show_play()

        choix_or_valid()

    move_player_with_choose(coordonnee_ligne, coordonnee_colonne)

def move_player_with_choose(coordonnee_ligne, coordonnee_colonne):
    show_play()
    while choix == "y":
        place_ia(coordonnee_colonne, coordonnee_ligne)
        show_play()
        bouton = int(input("Veuillez saisir:(8(haut),6(droite),4(gauche),2(bas):"))
        if bouton == 8 and coordonnee_ligne > 0:
            initialise_game(tableau)
            tableau[coordonnee_ligne - 1][coordonnee_colonne] = player
            tableau[coordonnee_ligne][coordonnee_colonne] = player
            coordonnee_ligne -= 1
            show_play()

        elif bouton == 6 and coordonnee_colonne < 2:
            initialise_game(tableau)
            tableau[coordonnee_ligne][coordonnee_colonne + 1] = player
            tableau[coordonnee_ligne][coordonnee_colonne] = player
            coordonnee_colonne += 1
            show_play()

        elif bouton == 4 and coordonnee_colonne > 0:
            initialise_game(tableau)
            tableau[coordonnee_ligne][coordonnee_colonne - 1] = player
            tableau[coordonnee_ligne][coordonnee_colonne] = player
            coordonnee_colonne -= 1
            show_play()

        elif bouton == 2 and coordonnee_ligne < 2:
            initialise_game(tableau)
            tableau[coordonnee_ligne + 1][coordonnee_colonne] = player
            tableau[coordonnee_ligne][coordonnee_colonne] = player
            coordonnee_ligne += 1
            show_play()

        choix_or_valid()

    move_player_before_chooce(coordonnee_ligne, coordonnee_colonne)


def Menue():
    print("- StartGame - Pour commancer le jeu")
    print("- RestartGame - Pour continuer le jeu que vous aviez commencer")
    print("  - Help - Pour obtenir de l'aide")
    commande = input("Veuiller saisir la commande de votre choix:")
    if commande == "StartGame" or commande == "startgame" or commande == "Startgame" or commande == "startGame":
        print("Vous avez saisit la commande startgame!")
        print("Démarrage de la nouvelle partie...")
        util_player()
        depart_player()
        choix_or_valid()
        move_player_before_chooce(coordonnee_ligne, coordonnee_colonne)

    elif commande == "RestartGame" or commande == "Restartgame" or commande == "restartgame" or commande == "restartGame":
        print("Vous avez choisit la commande RestartGame!")
        print("vous allez donc continuer votre partie précédente...")

    elif commande == "Help" or commande == "help":
        print("Vous avez saisie la commande 'Help'!")
        print("vous allez donc avoir de l'aide...")

    else:
        print("ERREUR!")
        Menue()


Menue()

