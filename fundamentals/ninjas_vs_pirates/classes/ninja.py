class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def Estado( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def Atacar( self , pirate ):
        pirate.health -= self.strength
        return self
    
    def Descansar ( self ):
        self.health += self.health/10