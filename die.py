from operator import imod
from random import randint

#Classe que representa um unico dado

class Die():

    #Supoe que seja um dado de seis lados
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    #Devolve um valor aleatorio entre 1 e o numero de lados
    def roll(self):
        return randint(1, self.num_sides)
    
    