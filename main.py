from code.Game import Game

#Criando classe da nave
class Nave:
    def __init__(self, age:int, name:str, atk:int, defense:int): # dizendo os parâmetros e seus tipos
        self.age = age # mostrando que "age" vai receber o valor do parametro age e que deve
        self.name = name
        self.atk = atk
        self.defense = defense

#herança
class Fuga (Nave): #Mostra herança quando uma classe é parâmetro da outra
    def __init__(self, age:int, name:str, atk:int, defense:int):
        super().__init__(age, name, atk, defense) # "Super" referencia a classe pai

#instanciando
t45 = Fuga(10,"Modelo T45", 70, 30)
print(t45.defense)

game = Game()
game.run()