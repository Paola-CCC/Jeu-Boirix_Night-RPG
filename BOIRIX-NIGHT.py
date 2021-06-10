import random
from random import randint
from random import randint, choice


# POUR M. JANIN : Pour comprendre le code il faut commencer par la fin.

class Monster:  # Class du Hero , qui contient les éléments qui vont être utilisés lors des combats : points d'attaques, points de vie , et inventaire. Ainsi on limite le nombre de fonctions.  Cette même classe est utilisée pour tous les niveaux qui impliquent Les ROVINOS = les méchants que doit battre BOB.
    def __init__(self, name, health_monster, healthMax_Monster, attack_Monster):
        self.name = name
        self._health_monster = health_monster
        self._healthMax_Monster = healthMax_Monster
        self._attack_Monster = attack_Monster

    def _get_health_Monster(self):
        return self._health_monster

    def _get_healthMax_Monster(self):
        return self._healthMax_Monster

    def _get_attack_Monster(self):
        return self._attack_Monster

    def _set_health_Monster(self, Nvlle_healthMonster):
        self._health_monster = Nvlle_healthMonster

    def _set_healthMax_Monster(self, Nvlle_healthMaxMonster):
        self._healthMax_Monster = Nvlle_healthMaxMonster

    def _set_attack_Monster(self, Rovi_Attaque):
        self._attack_Monster = Rovi_Attaque

    Vie_monstres = property(_get_health_Monster,
                            _set_health_Monster)  # Utilisations de proprités pour pouvoir modifier les attributs de la méthode _init_ . l'extérieur de la Classe.
    VieMax_monstres = property(_get_healthMax_Monster, _set_healthMax_Monster)
    Attacks_rovinos = property(_get_attack_Monster, _set_attack_Monster)


monstres = Monster("ROVINOS", 100, 100, 20)
monstres.name
monstres._health_monster
monstres._healthMax_Monster
monstres._attack_Monster


class BOB:  # Class du Hero , qui contient les éléments qui vont être utilisés lors des combats : points d'attaques, points de vie , et inventaire.
    def __init__(self, name, health, health_Max, inventaire, attack):
        self.name = name
        self._health = health
        self._health_Max = health_Max
        self._inventaire = inventaire
        self._attack = attack

    def Potion(self, potion):
        self._health = self._health + potion
        print(self._health)

    def _get_potion(self):
        return self.Potion

    def _set_potion(self, potionMagique):
        self.Potion = potionMagique

    def _get_health(self):
        return self._health

    def _get_health_Max(self):
        return self._health_Max

    def _get_inventaire(self):
        return self._inventaire

    def _get_attack(self):
        return self._attack

    def _set_health(self, Health):
        self._health = Health

    def _set_health_Max(self, Health_Max):
        self._health_Max = Health_Max

    def _set_inventaire(self, Nvlle_inventaire):
        self._inventaire = Nvlle_inventaire

    def _set_attack(self, Attacks):
        self._attack = Attacks

    Vie = property(_get_health,_set_health)  # Utilisations de proprités pour pouvoir modifier les attributs de la méthode _init_ . l'extérieur de la Classe.
    Vie_Max = property(_get_health_Max, _set_health_Max)
    Items = property(_get_inventaire, _set_inventaire)
    Degats = property(_get_attack, _set_attack)
    Bonus = property(_get_potion, _set_potion)


player = BOB("BOB", 100, 100, [], 0)
player.name
player._health
player._health_Max
player._inventaire
player._attack


def ChoixItems_Niv5():  # pour changer d'items au niveau 5
    print(" Vous avez actuellement dans votre inventaire :")
    print(player.Items)
    print(" Laquelle de ces armes souhaitez vous utiliser ?")
    print(" 1 : Couteau = 10 points d'attaques ")
    print(" 2 : Epée = 25 points d'attaques")
    print(" 3 : Potion Magique = +25 points de vie  ")
    choix_armes = str(input(" A vous de choisir "))
    if choix_armes == "1":
        player.Degats = 10
        print("Vous utilisez actuellement un Couteau avec 10 points d'attaques")
    elif choix_armes == "2":
        player.Degats = 25
        print("Vous utilisez actuellement une Épée avec 25 points d'attaques")
    elif choix_armes == "3":
        player.Potion(25)
        print("Vous venez d'utiliser une potion magique abvec avec 25 points de vie BONUS")
    else:
        pass


def ChoixItems_Niv3():  # pour changer d'items au niveau 3
    print(" Vous avez actuellement dans votre inventaire :")
    print(player.Items)
    print(" Laquelle de ces armes souhaitez vous utiliser ?")
    print(" 1 : Couteau = 20 points d'attaques ")
    print(" 2 : Epée = 25 points d'attaques")
    choix_armes = str(input(" A vous de choisir "))
    if choix_armes == "1":
        player.Degats = 20
    else:
        player.Degats = 25


def enigme():  # Niveau 1 = Enigme : La réponse est légende.
    print("==============================================================\n"
          "Pour avancer résolvez l'énigme suivante: \n"
          "Parfois loin de la réalité. \n"
          "Une image elle peut accompagner.\n "
          "La réponse ici trouvée; vous permettra peut-être d’y entrer. Qui est-elle ?\n"
          "==============================================================")
    reponse = str(input())
    if reponse.upper() == "LA LÉGENDE":
        player.Items.append("Couteau = 20 pts")
        player.Degats = 20
        print("Bien joué, vous avez gagné un nouvel objet :", player.Items)
        print("Vos points d'attaques:", player.Degats)
    else:
        while reponse.upper() != "LA LÉGENDE":
            print("Mauvaise réponse,l'énigme est trop difficile ? Voulez-vous des indices? Oui ou Non?")
            reponse = str(input())
            if reponse.upper() == "OUI":
                print("La bonne réponse est l'une des propositions:")
                print("1:L'histoire /Le conte / La légende")
                print("Réecrivez la bonne réponse")
                reponse = str(input())
                if reponse.upper() == "LA LÉGENDE":
                    print("Félicitation,la carte vous appartient")
                    player.Items.append("Couteau = 20 pts")
                    player.Degats = 20
                    print("Bien joué, vous avez gagné un nouvel objet :", player.Items)
                    print("Vos points d'attaques:", player.Degats)
                else:
                    print("C'est une mauvaise réponse,lisez bien l'énigme et réessayer")
            else:
                print("Réessayer")
                reponse = str(input())
                if reponse.upper() == "LA LÉGENDE":
                    player.Items.append("Couteau = 20 pts")
                    player.Degats = 20
                    print("Bien joué, vous avez gagné un nouvel objet :", player.Items)
                    print("Vos points d'attaques:", player.Degats)
                else:
                    print("Mauvaise réponse,réessayer")


def enigme2():
    print("Plus qu'une mission avant d'affronter le BOSS ROVINOS.\n "
          "A vous de résoudre cette enigme pour gagner des objets qui vous aiderons à le vaincre.\n "
          "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n"
          "L'énigme est la suivante:\n"
          "Mon premier est un mélange de terre et de pluie\n"
          "Mon deuxième vient après fa\n"
          "Mon tout ne perd jamais le nord\n"
          "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
    choix = str(input("A votre avis qui est-elle?"))
    while choix.upper() != "LA BOUSSOLE":
        print("non,reessayez")
        choix = str(input("Réessayez c'est facile!"))
    print("Félicitation,vous avez trouver la bonne réponse. Vous pouvez poursuivre votre route")


def FinNiv0():  # les FinNiv'  :Ce sont les inter-niveaux
    print("==========================================================================================")
    print("                BIENVENUE AU PREMIER NIVEAU                                              ")
    print("==========================================================================================")


def FinNiv1():
    print("==========================================================================================")
    print("   BIENVENUE dans le NIVEAU II   ")


def FinNiv2():
    print(" Vous avez un nouvel objet dans l'inventaire de BOB : Une Epée ")
    player.Items.append("Epée = 20 pts ")
    print(player.Items)
    monstres.Vie_monstres = 100
    player.Vie = 100
    monstres.Attacks_rovinos = 20
    print("==========================================================================================")
    print("   Bienvenue dans le NIVEAU III   ")  # Cloture le niveau 2 et ouvre niveau 3#


def FinNiv3():
    print("Deux nouveaux objets ont été rajouté dans l'inventaire de BOB : Potion Magique - a Usage unique- ")
    player.Items.append(" Potion Magique ")
    print(player.Items)
    monstres.Vie_monstres = 100
    player.Vie = 100
    monstres.Attacks_rovinos = 20
    print("==========================================================================================")
    print("   Bienvenue  dans le NIVEAU IV   ")  # Cloture le niveau 3 et ouvre niveau 4#


def FinNiv4():  # Cloture le niveau 4 et ouvre niveau 5#
    print(" BOB a obtenu un nouvel Item dans son inventaire : Carte Magique")
    player.Items.append("Carte Magique")
    print(player.Items)
    monstres.Vie_monstres = 100
    player.Vie = 100
    monstres.Attacks_rovinos = 25
    print("==========================================================================================")
    print("    Bienvenue dans le NIVEAU V : Vous êtes Face au BOSS ROVINOS ")


def FinNiv5():
    print("==========================================================================================")
    print(" Vous avez un nouvel objet dans l'inventaire de BOB : Une clé")
    player.Items.append("Clé")
    print(player.Items)
    print(" Souhaitez-vous utiliser la carte magique et la clé pour libérer les détenus ? ")
    print("1: OUI")
    print("2: NON ")
    choix_f = int(input(''))
    if choix_f == 1:
        print(player.Items)
        print(
            "BRAVOOO ! à vous et à BOB d'avoir fait preuve de tant de bravoure, vous avez utilisé votre carte magique et la clé pour libérer votre ami ainsi que les autres villageois.")
        print("MERCI A VOUS, A TRES BIENTOT POUR DE NOUVELLES AVENTURES ")
    elif choix_f == 2:
        print(" Dommage d'avoir renoncé en si bon chemin")
    else:
        print(" Dommage d'avoir renoncé en si bon chemin")


def BaisseVieMonster():  # fonction appelé dans les fonctions fight et fight_Final pour faire baisser la vie du Monstre
    base = 0
    if monstres.Vie_monstres > base:
        monstres.Vie_monstres = monstres.Vie_monstres - player.Degats
        return monstres.Vie_monstres
    else:
        print("BRAVOO ! Le Monstre a été vaincu par BOB")
        pass


def BaisseVieBOB():  # Fonction appelé dans les fonctions fight et fight_Final pour faire baisser la vie de BOB
    while player.Vie > 0:
        player.Vie = player.Vie - monstres.Attacks_rovinos
        return player.Vie


def fight_Final(base):  # Même logique que fight. La différence c'est qu'on peut changer d'armes au cours du combat.
    print("-- P : Pour Attaquer --")
    print("-- I : Pour afficher votre inventaire et changer d'armes --")
    choix = str(input(""))
    start = "P"
    objets = "I"
    i = base
    if choix.upper() == start:
        if i % 2 == 0:
            BaisseVieMonster()
            print(" Le BOSS ROVINOS est touché , il lui reste :", monstres._health_monster, " de point vie")
        else:
            BaisseVieBOB()
            print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de vie")

    elif choix.upper() == objets:
        ChoixItems_Niv5()
        print("Le combat reprend")
        print("P : Pour Attaquer ")
        choix = str(input(""))
        start = "P"
        i = base
        if choix.upper() == start:
            if i % 2 == 0:
                BaisseVieMonster()
                print(" Le BOSS ROVINOS est touché , il lui reste :", monstres._health_monster, " de point vie")
            else:
                BaisseVieBOB()
                print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de vie")
        else:
            print("ERREUR")
            choix = str(input(""))
            start = "P"
            i = base
            if choix.upper() == start:
                if i % 2 == 0:
                    BaisseVieMonster()
                    print(" Le ROVINOS est touché , il lui reste :", monstres._health_monster, " de point vie")
                else:
                    BaisseVieBOB()
                    print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de vie")
    else:
        print("Vous avez fait une erreur, Il faut toucher la touche P pour attaquer ")
        print("Le combat reprend")
        print("P : Pour Attaquer ")
        choix = str(input(""))
        start = "P"
        if choix.upper() == start:
            if i % 2 == 0:
                BaisseVieMonster()
                print(" Le ROVINOS est touché , il lui reste :", monstres._health_monster, " de point vie")
            else:
                BaisseVieBOB()
                print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de vie")
        else:
            print("ERREUR")
            choix = str(input(""))
            start = "P"
            i = base
            if choix.upper() == start:
                if i % 2 == 0:
                    BaisseVieMonster()
                    print(" Le ROVINOS est touché , il lui reste :", monstres._health_monster, " de point vie")
                else:
                    BaisseVieBOB()
                    print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de vie")


def fight(
        base):  # Le paramètre base = est le random. Il est stocké dans une variable. On demande à l'utilisateur de taper la touche P pour actionner le combat. Si cette variable est un multiple de 2 alors On utilise la fonction pour baisser la vie du monstre , Si ce n'est pas le cas on faisse la vie de BOB. S'il refuse on indique qu'il se trombe de touche et qu'il doit taper sur P.
    print("P : Pour Attaquer ")
    choix = str(input(""))
    start = "P"
    if choix.upper() == start:
        i = base
        if i % 2 == 0:
            BaisseVieMonster()
            print(" Le ROVINOS est touché , il lui reste :", monstres._health_monster, " de point vie")
        else:
            BaisseVieBOB()
            print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de vie")
    else:
        print("Vous avez fait une erreur, Il faut toucher la touche P")
        print("P : Pour Attaquer ")
        choix = str(input(""))
        start = "P"
        if choix.upper() == start:
            i = base
            if i % 2 == 0:
                BaisseVieMonster()
                print(" Le ROVINOS est touché , il lui reste :", monstres._health_monster, " de point vie")
            else:
                BaisseVieBOB()
                print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de vie")
        else:
            print(" ERREUR ")
            choix = str(input(""))
            start = "P"
            if choix.upper() == start:
                i = base
                if i % 2 == 0:
                    BaisseVieMonster()
                    print(" Le ROVINOS est touché , il lui reste :", monstres._health_monster, " de point vie")
                else:
                    BaisseVieBOB()
                    print("Attention , Le ROVINOS a touché BOB, il lui reste : ", player._health, "de point de vie")


def Combat_niv5():
    print("BOB est face à un ROVINOS ")
    print("1: Combattre le ROVINOS ")
    print("2: Afficher l'inventaire et Changer d'armes")
    choix_c = str(input())
    if choix_c == "1":
        while player.Vie and monstres.Vie_monstres > 0:
            fight_Final(random.randint(1, 100))
            # Nous avons utilisé le random comme un argument, avec comme idée que tant que la vie du monstre et de bOb sont supérieur à 0 alors on utilise la fonction combat du niveau = final fight  #
    elif choix_c == "2":
        ChoixItems_Niv5()
        while player.Vie and monstres.Vie_monstres > 0:
            fight_Final(random.randint(1, 100))
    else:
        print("Merci de respecter les touches indiquées.")
        ChoixItems_Niv5
        while player.Vie and monstres.Vie_monstres > 0:
            fight_Final(random.randint(1, 100))


def Combat_niv3():
    print("BOB est face à un ROVINOS ")
    print("1: Combattre le ROVINOS ")
    print("2: Afficher l'inventaire et/ou Changer d'armes")
    choix_c = str(input())
    if choix_c == "1":
        while player.Vie and monstres.Vie_monstres > 0:
            fight(random.randint(1, 100))
            # Nous avons utilisé le random comme un argument, avec comme idée que tant que la vie du monstre et de bOb sont supérieur à 0 alors on utilise la fonction combat du niveau = fight #

    elif choix_c == "2":
        ChoixItems_Niv3()
        while player.Vie and monstres.Vie_monstres > 0:
            fight(random.randint(1, 100))
    else:
        print("Merci de respecter les touches indiquées.")
        ChoixItems_Niv3()
        while player.Vie and monstres.Vie_monstres > 0:
            fight(random.randint(1, 100))


def Combat_niv2():
    print("BOB est face à un ROVINOS ")
    print("1: Combattre le ROVINOS ")
    print("2: Afficher l'inventaire ")
    choix_c = str(input())
    if choix_c == "1":
        while player.Vie and monstres.Vie_monstres > 0:
            fight(random.randint(1, 100))
            # Nous avons utilisé le random comme un argument, avec comme idée que tant que la vie du monstre et de bOb sont supérieur à 0 alors on utilise la fonction combat du niveau = fight #
    elif choix_c == "2":
        print(player.Items)
        while player.Vie and monstres.Vie_monstres > 0:
            fight(random.randint(1, 100))
    else:
        print("Merci de respecter les touches indiquées.")
        print(player.Items)
        while player.Vie and monstres.Vie_monstres > 0:
            fight(random.randint(1, 100))


def Recommencer_Niv5():  # Fonction qui permet de recommencer le niveau 3#
    print("BOB vient de perdre son combat contre un Rovinos et est mort !! ")
    print("Que souhaitez-vous ? ")
    print("1 : Pour  Recommencer ")
    print("2 : Pour Retourner au Menu ")
    choix = str(input(" "))
    if choix == "1":
        monstres.Vie_monstres = 100
        player.Vie = 100
        Combat_niv5()  # On fait appel à la fonction combat du niveau qu'on a voulu refaire#
        if player.Vie > 0:
            FinNiv5()
    elif choix == "2":
        player.Vie = 100
        Menu()
    else:
        player.Vie = 100
        Menu()


def Recommencer_Niv3():  # Fonction qui permet de recommencer le niveau 3#
    print("BOB vient de perdre son combat contre un Rovinos et est mort !! ")
    print("Que souhaitez-vous ? ")
    print("1 : Pour  Recommencer ")
    print("2 : Pour Retourner au Menu ")
    choix = str(input(" "))
    if choix == "1":
        monstres.Vie_monstres = 100
        player.Vie = 100
        Combat_niv3()  # On fait appel à la fonction combat du niveau qu'on a voulu refaire
        if player.Vie > 0:  # Condition à respecter pour aller aux niveaux suivants
            FinNiv3()
            enigme2()  # <--- Enigme Niv 4
            FinNiv4()
            Combat_niv5()
            if player.Vie > 0:
                FinNiv5()
            else:
                while player.Vie == 0:
                    Recommencer_Niv5()
    elif choix == "2":
        player.Vie = 100
        Menu()
    else:
        player.Vie = 100
        Menu()


def Recommencer_Niv2():  # Fonction qui permet de recommencer le niveau 2#
    print("BOB vient de perdre son combat contre un Rovinos et est mort !! ")
    print("Que souhaitez-vous ? ")
    print("1 : Pour  Recommencer ")
    print("2 : Pour Retourner au Menu ")
    choix = str(input(" "))
    if choix == "1":
        monstres.Vie_monstres = 100
        player.Vie = 100
        Combat_niv2()  # On fait appel à la fonction combat du niveau qu'on a voulu refaire
        if player.Vie > 0:
            FinNiv2()
            Combat_niv3()  # Combat Niveau 3#
            if player.Vie > 0:
                FinNiv3()
                enigme2()  # Enigme Niv 4
                FinNiv4()
                Combat_niv5()  # <--- Combat Niv 5
                if player.Vie > 0:
                    FinNiv5()
                else:
                    while player.Vie == 0:
                        Recommencer_Niv5()
            else:
                while player.Vie == 0:
                    Recommencer_Niv3()

    elif choix == "2":
        player.Vie = 100
        Menu()
    else:
        player.Vie = 100
        Menu()


def AskName():
    print("Quelle est votre Prénom ?")
    global Name_Joueur
    Name_Joueur = input("")
    return Name_Joueur


def Description():  # Description de l'histoire.
    S = ("=========================================================================================================\n"
         "|Situé à proximité de la forêt LINGARIU, où vivent les monstres BOB prend son sac à dos et pénètre      |\n"
         "|dans la fôret.Le village BOIRIX subit une attaque des géants des bois les ROVINOS.                     |\n"
         "|Ces démons mi-hommes mi-bêtes attaquent, ravagent le village, détruisent les récoltes, mettant celui-ci|\n"
         "|à feu et à sang.                                                                                       |\n"
         "|Dans cette nuit d’horreur les villageois qui n’ont pas été dévoré et qui n’ont pas pu se cacher sont   |\n"
         "|emportés et kidnappés par ces bêtes. BOB un villageois de BOIRIX a décidé de braver sa peur et s’est   |\n"
         "|proposé pour aller chercher son ami JEAN MARC kidnappé llageois.    lui aussi ainsi que les autres vi  |\n"
         "=========================================================================================================")
    print("Taper 1: Suivant")
    print("Taper 2: Retour")
    Choix = input("Que choissiez-vous ?")
    if Choix == "1":
        print(S)
        print("--> Votre mission :", Name_Joueur,
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
        FinNiv0()
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
        FinNiv1()
        Combat_niv2()  # combat Niveau2#
        if player.Vie > 0:
            FinNiv2()
            Combat_niv3()  # combat Niveau 3#
            if player.Vie > 0:
                FinNiv3()
                enigme2()  # <--- Enigme Niv 4#
                FinNiv4()
                Combat_niv5()
                if player.Vie > 0:  # Combat final##Combat Niveau3#
                    FinNiv5()
                else:
                    while player.Vie == 0:
                        Recommencer_Niv5()
            else:
                while player.Vie == 0:
                    Recommencer_Niv3()
        else:
            while player.Vie == 0:
                Recommencer_Niv2()

    elif Choix == "2":
        Menu()
    else:
        Menu()


def PlayGame():
    print("Bienvenue dans BOIRIX NIGHT ")
    AskName()
    Description()


def About():
    print(
        "Voici BOIRIX NIGHT , Le Jeu de L'année 2020/2021 développé par les étudiants Ibrahim, Tania et Paola de l'Ecole HETIC")
    Menu()


def Exit():
    pass


def Menu():
    print("1: Create new game")
    print("2: About")
    print("3: Exit")
    Choix = str(input())
    if Choix == "1":
        PlayGame()
    elif Choix == "2":
        About()
    else:
        Exit()


Menu()
