import math
#capacidade=5 conforme a informação dada 
def carros(pessoas, capacidade=5):
    #arredonda a quantidade de carros para cima, resolvendo os casos do tipo pessoas=11 e capacidade=5
    return math.ceil(pessoas/capacidade)