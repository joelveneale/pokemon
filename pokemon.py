
class Pokemon:
    def __init__(self, name, level, type, is_knocked_out):
        self.name = name
        self.level = level
        self.type = type
        self.is_knocked_out = is_knocked_out
        self.exp = 0
        self.max_health = level
        self.health = self.max_health

    def __repr__(self):
        return "Pokemon info. {}, current level: {}, type: {}, maximun health: {}, current health: {}.\n".format(
            self.name, self.level, self.type, self.max_health, self.health)

    def lose_health(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.health = 0
            self.knockout()


    def gain_health(self, heal):
        self.health += heal
        if self.health >= self.max_health:
            self.health = self.max_health
        print("{} gained {} health".format(self.name, heal))
        print("{}'s health: {}".format(self.name, self.health))

    def knockout(self):
        if self.is_knocked_out:
            print("{name} is already knocked out.".format(name=self.name))
        else:
            self.is_knocked_out = True
            print("{name} is knocked out!".format(name=self.name))

    def revive(self):
        if self.is_knocked_out:
            self.is_knocked_out = False
            self.health = 1
            print("{name} has been revived with {health} health!".format(name=self.name, health=self.health))
            else:
            print("{name} is not knocked out.".format(name=self.name))

