
from perso_bob import BOB
from rovinos import Monster
import random
from random import randint
from random import randint, choice


player = BOB("BOB", 100, 100, [], 0)
player.name
player._health
player._health_max
player._inventaire
player._attack



monsters = Monster("ROVINOS", 100, 100, 20)
monsters.name
monsters._health_monster
monsters._health_max_monster
monsters._attack_monster








def choice_items_level5():  # pour changer d'items au niveau 5
    print(" Vous avez actuellement dans votre inventaire :")
    print(player.items)
    print(" Laquelle de ces armes souhaitez vous utiliser ?")
    print(" 1 : Couteau = 10 points d'attaques ")
    print(" 2 : Epée = 25 points d'attaques")
    print(" 3 : potion Magique = +25 points de life  ")
    choice_weapons = str(input(" A vous de choisir "))
    if choice_weapons == "1":
        player.damage = 10
        print("Vous utilisez actuellement un Couteau avec 10 points d'attaques")
    elif choice_weapons == "2":
        player.damage = 25
        print("Vous utilisez actuellement une Épée avec 25 points d'attaques")
    elif choice_weapons == "3":
        player.potion(25)
        print("Vous venez d'utiliser une potion magique abvec avec 25 points de life BONUS")
    else:
        pass


def choice_items_level3():  # pour changer d'items au niveau 3
    print(" Vous avez actuellement dans votre inventaire :")
    print(player.items)
    print(" Laquelle de ces armes souhaitez vous utiliser ?")
    print(" 1 : Couteau = 20 points d'attaques ")
    print(" 2 : Epée = 25 points d'attaques")
    choice_weapons = str(input(" A vous de choisir "))
    if choice_weapons == "1":
        player.damage = 20
    else:
        player.damage = 25


def enigme():  # Niveau 1 = Enigme : La réponse est légende.
    print("==============================================================\n"
          "Pour avancer résolvez l'énigme suivante: \n"
          "Parfois loin de la réalité. \n"
          "Une image elle peut accompagner.\n "
          "La réponse ici trouvée; vous permettra peut-être d’y entrer. Qui est-elle ?\n"
          "==============================================================")
    answer = str(input())
    if answer.upper() == "LA LÉGENDE":
        player.items.append("Couteau = 20 pts")
        player.damage = 20
        print("Bien joué, vous avez gagné un nouvel objet :", player.items)
        print("Vos points d'attaques:", player.damage)
    else:
        while answer.upper() != "LA LÉGENDE":
            print("Mauvaise réponse,l'énigme est trop difficile ? Voulez-vous des indices? Oui ou Non?")
            answer = str(input())
            if answer.upper() == "OUI":
                print("La bonne réponse est l'une des propositions:")
                print("1:L'histoire /Le conte / La légende")
                print("Réecrivez la bonne réponse")
                answer = str(input())
                if answer.upper() == "LA LÉGENDE":
                    print("Félicitation,la carte vous appartient")
                    player.items.append("Couteau = 20 pts")
                    player.damage = 20
                    print("Bien joué, vous avez gagné un nouvel objet :", player.items)
                    print("Vos points d'attaques:", player.damage)
                else:
                    print("C'est une mauvaise réponse,lisez bien l'énigme et réessayer")
            else:
                print("Réessayer")
                answer = str(input())
                if answer.upper() == "LA LÉGENDE":
                    player.items.append("Couteau = 20 pts")
                    player.damage = 20
                    print("Bien joué, vous avez gagné un nouvel objet :", player.items)
                    print("Vos points d'attaques:", player.damage)
                else:
                    print("Mauvaise réponse,réessayer")


def enigme_2():
    print("Plus qu'une mission avant d'affronter le BOSS ROVINOS.\n "
          "A vous de résoudre cette enigme pour gagner des objets qui vous aiderons à le vaincre.\n "
          "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n"
          "L'énigme est la suivante:\n"
          "Mon premier est un mélange de terre et de pluie\n"
          "Mon deuxième lifent après fa\n"
          "Mon tout ne perd jamais le nord\n"
          "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
    choice = str(input("A votre avis qui est-elle?"))
    while choice.upper() != "LA BOUSSOLE":
        print("non,reessayez")
        choice = str(input("Réessayez c'est facile!"))
    print("Félicitation,vous avez trouver la bonne réponse. Vous pouvez poursuivre votre route")


def end_level0():  # les end_level'  :Ce sont les inter-niveaux
    print("==========================================================================================")
    print("                BIENVENUE AU PREMIER NIVEAU                                              ")
    print("==========================================================================================")


def end_level1():
    print("==========================================================================================")
    print("   BIENVENUE dans le NIVEAU II   ")


def end_level2():
    print(" Vous avez un nouvel objet dans l'inventaire de BOB : Une Epée ")
    player.items.append("Epée = 20 pts ")
    print(player.items)
    monsters.life_monster = 100
    player.life = 100
    monsters.attack_rovinos = 20
    print("==========================================================================================")
    print("   Bienvenue dans le NIVEAU III   ")  # Cloture le niveau 2 et ouvre niveau 3#


def end_level3():
    print("Deux nouveaux objets ont été rajouté dans l'inventaire de BOB : potion Magique - a Usage unique- ")
    player.items.append(" potion Magique ")
    print(player.items)
    monsters.life_monster = 100
    player.life = 100
    monsters.attack_rovinos = 20
    print("==========================================================================================")
    print("   Bienvenue  dans le NIVEAU IV   ")  # Cloture le niveau 3 et ouvre niveau 4#


def end_level4():  # Cloture le niveau 4 et ouvre niveau 5#
    print(" BOB a obtenu un nouvel Item dans son inventaire : Carte Magique")
    player.items.append("Carte Magique")
    print(player.items)
    monsters.life_monster = 100
    player.life = 100
    monsters.attack_rovinos = 25
    print("==========================================================================================")
    print("    Bienvenue dans le NIVEAU V : Vous êtes Face au BOSS ROVINOS ")


def end_level5():
    print("==========================================================================================")
    print(" Vous avez un nouvel objet dans l'inventaire de BOB : Une clé")
    player.items.append("Clé")
    print(player.items)
    print(" Souhaitez-vous utiliser la carte magique et la clé pour libérer les détenus ? ")
    print("1: OUI")
    print("2: NON ")
    choice_f = int(input(''))
    if choice_f == 1:
        print(player.items)
        print(
            "BRAVOOO ! à vous et à BOB d'avoir fait preuve de tant de bravoure, vous avez utilisé votre carte magique et la clé pour libérer votre ami ainsi que les autres villageois.")
        print("MERCI A VOUS, A TRES BIENTOT POUR DE NOUVELLES AVENTURES ")
    elif choice_f == 2:
        print(" Dommage d'avoir renoncé en si bon chemin")
    else:
        print(" Dommage d'avoir renoncé en si bon chemin")




def fight_final(base):  # Même logique que fight. La différence c'est qu'on peut changer d'armes au cours du combat.
    print("-- P : Pour Attaquer --")
    print("-- I : Pour afficher votre inventaire et changer d'armes --")
    choice = str(input(""))
    start = "P"
    objets = "I"
    i = base
    if choice.upper() == start:
        if i % 2 == 0:
            monsters.decrease_life_monster(player.damage)
            print(" Le BOSS ROVINOS est touché , il lui reste :", monsters._health_monster, " de point de vie")
        else:
            player.decrease_life_bob(monsters.attack_rovinos)
            print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de life")

    elif choice.upper() == objets:
        choice_items_level5()
        print("Le combat reprend")
        print("P : Pour Attaquer ")
        choice = str(input(""))
        start = "P"
        i = base
        if choice.upper() == start:
            if i % 2 == 0:
                monsters.decrease_life_monster(player.damage)
                print(" Le BOSS ROVINOS est touché , il lui reste :", monsters._health_monster, " de point de vie")
            else:
                player.decrease_life_bob(monsters.attack_rovinos)
                print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de life")
        else:
            print("ERREUR")
            choice = str(input(""))
            start = "P"
            i = base
            if choice.upper() == start:
                if i % 2 == 0:
                    monsters.decrease_life_monster(player.damage)
                    print(" Le ROVINOS est touché , il lui reste :", monsters._health_monster, " de point de vie")
                else:
                    player.decrease_life_bob(monsters.attack_rovinos)
                    print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de life")
    else:
        print("Vous avez fait une erreur, Il faut toucher la touche P pour attaquer ")
        print("Le combat reprend")
        print("P : Pour Attaquer ")
        choice = str(input(""))
        start = "P"
        if choice.upper() == start:
            if i % 2 == 0:
                monsters.decrease_life_monster(player.damage)
                print(" Le ROVINOS est touché , il lui reste :", monsters._health_monster, " de point de vie")
            else:
                player.decrease_life_bob(monsters.attack_rovinos)
                print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de life")
        else:
            print("ERREUR")
            choice = str(input(""))
            start = "P"
            i = base
            if choice.upper() == start:
                if i % 2 == 0:
                    monsters.decrease_life_monster(player.damage)
                    print(" Le ROVINOS est touché , il lui reste :", monsters._health_monster, " de point de vie")
                else:
                    player.decrease_life_bob(monsters.attack_rovinos)
                    print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de life")


def fight(base):  # Le paramètre base = est le random. Il est stocké dans une variable. On demande à l'utilisateur de taper la touche P pour actionner le combat. Si cette variable est un multiple de 2 alors On utilise la fonction pour baisser la life du monstre , Si ce n'est pas le cas on faisse la life de BOB. S'il refuse on indique qu'il se trombe de touche et qu'il doit taper sur P.
    print("P : Pour Attaquer ")
    choice = str(input(""))
    start = "P"
    if choice.upper() == start:
        i = base
        if i % 2 == 0:
            monsters.decrease_life_monster(player.damage)
            print(" Le ROVINOS est touché , il lui reste :", monsters._health_monster, " de point de vie")
        else:
            player.decrease_life_bob(monsters.attack_rovinos)
            print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de life")
    else:
        print("Vous avez fait une erreur, Il faut toucher la touche P")
        print("P : Pour Attaquer ")
        choice = str(input(""))
        start = "P"
        if choice.upper() == start:
            i = base
            if i % 2 == 0:
                monsters.decrease_life_monster(player.damage)
                print(" Le ROVINOS est touché , il lui reste :", monsters._health_monster, " de point de vie")
            else:
                player.decrease_life_bob(monsters.attack_rovinos)
                print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de life")
        else:
            print(" ERREUR ")
            choice = str(input(""))
            start = "P"
            if choice.upper() == start:
                i = base
                if i % 2 == 0:
                    monsters.decrease_life_monster(player.damage)
                    print(" Le ROVINOS est touché , il lui reste :", monsters._health_monster, " de point de vie")
                else:
                    player.decrease_life_bob(monsters.attack_rovinos)
                    print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de life")


def fight_level5():
    print("BOB est face à un ROVINOS ")
    print("1: Combattre le ROVINOS ")
    print("2: Afficher l'inventaire et Changer d'armes")
    choice_c = str(input())
    if choice_c == "1":
        while player.life and monsters.life_monster > 0:
            fight_final(random.randint(1, 100))
            # Nous avons utilisé le random comme un argument, avec comme idée que tant que la life du monstre et de bOb sont supérieur à 0 alors on utilise la fonction combat du niveau = final fight  #
    elif choice_c == "2":
        choice_items_level5()
        while player.life and monsters.life_monster > 0:
            fight_final(random.randint(1, 100))
    else:
        print("Merci de respecter les touches indiquées.")
        choice_items_level5
        while player.life and monsters.life_monster > 0:
            fight_final(random.randint(1, 100))


def fight_level3():
    print("BOB est face à un ROVINOS ")
    print("1: Combattre le ROVINOS ")
    print("2: Afficher l'inventaire et/ou Changer d'armes")
    choice_c = str(input())
    if choice_c == "1":
        while player.life and monsters.life_monster > 0:
            fight(random.randint(1, 100))
            # Nous avons utilisé le random comme un argument, avec comme idée que tant que la life du monstre et de bOb sont supérieur à 0 alors on utilise la fonction combat du niveau = fight #

    elif choice_c == "2":
        choice_items_level3()
        while player.life and monsters.life_monster > 0:
            fight(random.randint(1, 100))
    else:
        print("Merci de respecter les touches indiquées.")
        choice_items_level3()
        while player.life and monsters.life_monster > 0:
            fight(random.randint(1, 100))


def fight_level2():
    print("BOB est face à un ROVINOS ")
    print("1: Combattre le ROVINOS ")
    print("2: Afficher l'inventaire ")
    choice_c = str(input())
    if choice_c == "1":
        while player.life and monsters.life_monster > 0:
            fight(random.randint(1, 100))
            # Nous avons utilisé le random comme un argument, avec comme idée que tant que la life du monstre et de bOb sont supérieur à 0 alors on utilise la fonction combat du niveau = fight #
    elif choice_c == "2":
        print(player.items)
        while player.life and monsters.life_monster > 0:
            fight(random.randint(1, 100))
    else:
        print("Merci de respecter les touches indiquées.")
        print(player.items)
        while player.life and monsters.life_monster > 0:
            fight(random.randint(1, 100))


def restart_level5():  # Fonction qui permet de recommencer le niveau 3#
    print("BOB lifent de perdre son combat contre un Rovinos et est mort !! ")
    print("Que souhaitez-vous ? ")
    print("1 : Pour  Recommencer ")
    print("2 : Pour Retourner au Menu ")
    choice = str(input(" "))
    if choice == "1":
        monsters.life_monster = 100
        player.life = 100
        fight_level5()  # On fait appel à la fonction combat du niveau qu'on a voulu refaire#
        if player.life > 0:
            end_level5()
    elif choice == "2":
        player.life = 100
        Menu()
    else:
        player.life = 100
        Menu()


def restart_level3():  # Fonction qui permet de recommencer le niveau 3#
    print("BOB lifent de perdre son combat contre un Rovinos et est mort !! ")
    print("Que souhaitez-vous ? ")
    print("1 : Pour  Recommencer ")
    print("2 : Pour Retourner au Menu ")
    choice = str(input(" "))
    if choice == "1":
        monsters.life_monster = 100
        player.life = 100
        fight_level3()  # On fait appel à la fonction combat du niveau qu'on a voulu refaire
        if player.life > 0:  # Condition à respecter pour aller aux niveaux suivants
            end_level3()
            enigme_2()  # <--- Enigme Niv 4
            end_level4()
            fight_level5()
            if player.life > 0:
                end_level5()
            else:
                while player.life == 0:
                    restart_level5()
    elif choice == "2":
        player.life = 100
        Menu()
    else:
        player.life = 100
        Menu()


def restart_level2():  # Fonction qui permet de recommencer le niveau 2#
    print("BOB lifent de perdre son combat contre un Rovinos et est mort !! ")
    print("Que souhaitez-vous ? ")
    print("1 : Pour  Recommencer ")
    print("2 : Pour Retourner au Menu ")
    choice = str(input(" "))
    if choice == "1":
        monsters.life_monster = 100
        player.life = 100
        fight_level2()  # On fait appel à la fonction combat du niveau qu'on a voulu refaire
        if player.life > 0:
            end_level2()
            fight_level3()  # Combat Niveau 3#
            if player.life > 0:
                end_level3()
                enigme_2()  # Enigme Niv 4
                end_level4()
                fight_level5()  # <--- Combat Niv 5
                if player.life > 0:
                    end_level5()
                else:
                    while player.life == 0:
                        restart_level5()
            else:
                while player.life == 0:
                    restart_level3()

    elif choice == "2":
        player.life = 100
        Menu()
    else:
        player.life = 100
        Menu()


def AskName():
    print("Quelle est votre Prénom ?")
    global name_player
    name_player = input("")
    return name_player


def description():  # description de l'histoire.
    S = ("=========================================================================================================\n"
         "|Situé à proximité de la forêt LINGARIU, où vivent les monsters BOB prend son sac à dos et pénètre      |\n"
         "|dans la fôret.Le village BOIRIX subit une attaque des géants des bois les ROVINOS.                     |\n"
         "|Ces démons mi-hommes mi-bêtes attaquent, ravagent le village, détruisent les récoltes, mettant celui-ci|\n"
         "|à feu et à sang.                                                                                       |\n"
         "|Dans cette nuit d’horreur les villageois qui n’ont pas été dévoré et qui n’ont pas pu se cacher sont   |\n"
         "|emportés et kidnappés par ces bêtes. BOB un villageois de BOIRIX a décidé de braver sa peur et s’est   |\n"
         "|proposé pour aller chercher son ami JEAN MARC kidnappé llageois.    lui aussi ainsi que les autres vi  |\n"
         "=========================================================================================================")
    print("Taper 1: Suivant")
    print("Taper 2: Retour")
    choice = input("Que choissiez-vous ?")
    if choice == "1":
        print(S)
        print("--> Votre mission :", name_player,
              "," "Aider BOB à sauver les villageois en vainquant les ROVINOS ! <--")
        map2 = ["  Niveau 1---------------      -------------------------------",
                "-     ----           ----------       ------------------------",
                "--                Niveau2              -------------        --",
                "-       ------                                          ------",
                "-                           ----------  Niveau 3         -----",
                "----                                                        --",
                "-------        ---   Niveau 4         --------              --",
                "-  -                                  ------                --",
                "------    --------------                                     -",
                "----  ----------------------------         Combat avec le boss"]
        for i in map2:
            print(i)

        print("AIDEZ VOUS DE LA CARTE POUR AVANCER JUSQU'A JEAN MARC ")
        end_level0()
        map = ["B  * *****", "*     ****",
               "**  *  * *", "*     ****",
               "*     ** *", "****     *",
               "***** *  *", "* *      *",
               "* ***    *", "* *****   Arrivée"]
        for i in map:
            print(i)  # Labyrinthe pour aller jusqu'au Niveau 1.

        x = 0
        y = 0

        def replace(ligne, i, B):
            s = ligne[:i] + B + ligne[i + 1:]
            return s

        def display(map):
            for j in map[: len(map)]:
                print(j)

        while (x != 9) or (y != 9):
            pos = input(
                "Dans quelle direction Bob doit-il se diriger? :(g: à gauche, d: à droite, h: en haut, b: en bas )")
            if pos == "h":
                if map[x - 1][y] == "*":
                    print("--------->Bob ne peut pas aller vers le haut, il y'a un obstacle!<---------")
                elif map[x - 1][y] == " ":
                    map[x - 1] = replace(map[x - 1], y, "B")
                    map[x] = replace(map[x], y, " ")
                    x = x - 1
            if pos == "b":
                if map[x + 1][y] == "*":
                    print("--------->Bob ne peut pas aller vers le bas, il y'a un obstacle!<---------")
                elif map[x + 1][y] == " ":
                    map[x + 1] = replace(map[x + 1], y, "B")
                    map[x] = replace(map[x], y, " ")
                    x = x + 1
            if pos == "d":
                if map[x][y + 1] == "*":
                    print("--------->Bob ne peut pas passer à droite!<---------")
                elif map[x][y + 1] == " ":
                    map[x] = replace(map[x], y + 1, "B")
                    map[x] = replace(map[x], y, " ")
                    y = y + 1
            if pos == "g":
                if map[x][y - 1] == "*":
                    print("--------->Bob ne peut pas passer à gauche!<---------")
                elif map[x][y - 1] == " ":
                    map[x] = replace(map[x], y - 1, "B")
                    map[x] = replace(map[x], y, " ")  # pour effacer l'ancienne position de Bob
                    y = y - 1

            display(map)

        print("~~~~~~\n"
              "Bravo!")

        enigme()  # <--- niv 1#
        end_level1()
        fight_level2()  # combat Niveau2#
        if player.life > 0:
            end_level2()
            fight_level3()  # combat Niveau 3#
            if player.life > 0:
                end_level3()
                enigme_2()  # <--- Enigme Niv 4#
                end_level4()
                fight_level5()
                if player.life > 0:  # Combat final##Combat Niveau3#
                    end_level5()
                else:
                    while player.life == 0:
                        restart_level5()
            else:
                while player.life == 0:
                    restart_level3()
        else:
            while player.life == 0:
                restart_level2()

    elif choice == "2":
        Menu()
    else:
        Menu()


def play_game():
    print("Bienvenue dans BOIRIX NIGHT ")
    AskName()
    description()


def about():
    print("Voici BOIRIX NIGHT , Le Jeu de L'année 2020/2021 développé par les étudiants Paola,Tania & Ibrahim de l'Ecole HETIC")
    Menu()


def exit():
    pass


def Menu():
    print("1: Create new game")
    print("2: About")
    print("3: Exit")
    choice = str(input())
    if choice == "1":
        play_game()
    elif choice == "2":
        about()
    else:
       exit()


Menu()
