import random
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
    
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return super().attack()
        
    def receiveDamage(self, damage):
        self.health=self.health-damage
        if self.health != 0:
            return str(self.name) + " has received " + str(damage) + " points of damage"
        else:
            return str(self.name)+ " has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"



# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health=self.health-damage
        if self.health != 0:
            return "A Saxon has received "+ str(damage) +  " points of damage"
        else:
            return "A Saxon has died in combat"




# War


class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    def addViking(self,Viking):
        self.Viking= Viking
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.Saxon= Saxon
        self.saxonArmy.append(Saxon)

    def VikingAtack(self):
        Saxon.receiveDamage = random
        if Saxon[0]==0:   
            self.saxonArmy.pop()
        return "result of calling " + Saxon.receiveDamage()+ " of a "+ self.Saxon + " with the " + Viking.attack() +" of a Viking"

    def SaxonAttack(self):
        Viking.receiveDamage = Saxon.attack()
        if Viking[0]==0:
            self.vikingArmy.pop()
        return "result of calling " + Viking.receiveDamage()+ " of a "+ Viking.__name__ + " with the " + Saxon.attack() +" of a Saxon"

    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy)== 0:
            return "Vikings have won the war of the century"
        else:
            return "Vikings and Saxons are still in the thick of battle."
    

