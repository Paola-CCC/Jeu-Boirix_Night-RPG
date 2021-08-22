
import perso_bob 




class Monster:  # Class du Hero , qui contient les éléments qui vont être utilisés lors des combats : points d'attaques, points de life , et inventaire. Ainsi on limite le nombre de fonctions.  Cette même classe est utilisée pour tous les niveaux qui impliquent Les ROVINOS = les méchants que doit battre BOB.
    def __init__(self, name, health_monster, healthMax_Monster, attack_monster):
        self.name = name
        self._health_monster = health_monster
        self._health_max_monster = healthMax_Monster
        self._attack_monster = attack_monster

    def _get_health_monster(self):
        return self._health_monster

    def _get_health_max_monster(self):
        return self._health_max_monster

    def _get_attack_monster(self):
        return self._attack_monster

    def _set_health_Monster(self, new_health_monster):
        self._health_monster = new_health_monster

    def _set_health_max_monster(self, new_health_max_monster):
        self._health_max_monster = new_health_max_monster

    def _set_attack_monster(self, rovinos_attack):
        self._attack_monster = rovinos_attack

    def decrease_life_monster(self,damage):  # fonction appelé dans les fonctions fight et fight_final pour faire baisser la life du Monstre
        base = 0
        if self._health_monster > base:
            self._health_monster = self._health_monster - damage
            return self._health_monster
        else:
            print("BRAVOO ! Le Monstre a été vaincu par BOB")
            pass

    life_monster = property(_get_health_monster, _set_health_Monster)  # Utilisations de proprités pour pouvoir modifier les attributs de la méthode _init_ . l'extérieur de la Classe.
    life_max_monsters = property(_get_health_max_monster, _set_health_max_monster)
    attack_rovinos = property(_get_attack_monster, _set_attack_monster)


