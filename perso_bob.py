import rovinos

class BOB:  # Class du Hero , qui contient les éléments qui vont être utilisés lors des combats : points d'attaques, points de life , et inventaire.
    def __init__(self, name, health, health_max, inventaire, attack):
        self.name = name
        self._health = health
        self._health_max = health_max
        self._inventaire = inventaire
        self._attack = attack

    def potion(self, potion):
        self._health = self._health + potion
        print(self._health)
    

    def decrease_life_bob(self, degats):
        while self._health > 0:
            self._health = self._health - degats
            return self._health


    def _get_potion(self):
        return self.potion

    def _set_potion(self, potionMagique):
        self.potion = potionMagique

    def _get_health(self):
        return self._health

    def _get_health_max(self):
        return self._health_max

    def _get_inventaire(self):
        return self._inventaire

    def _get_attack(self):
        return self._attack

    def _set_health(self, health):
        self._health = health

    def _set_health_max(self, health_max):
        self._health_max = health_max

    def _set_inventaire(self,new_inventaire):
        self._inventaire = new_inventaire

    def _set_attack(self, attack):
        self._attack = attack

    life = property(_get_health,_set_health)  # Utilisations de proprités pour pouvoir modifier les attributs de la méthode _init_ . l'extérieur de la Classe.
    life_max = property(_get_health_max, _set_health_max)
    items = property(_get_inventaire, _set_inventaire)
    damage = property(_get_attack, _set_attack)
    Bonus = property(_get_potion, _set_potion)








# monsters.decrease_life_monster()

# player.decrease_life_bob()