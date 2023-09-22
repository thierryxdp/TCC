from math import ceil
def carros (pessoas, capacidade=5):
        'retorna a quantidade necessária de carros paa comportar certo numero de pessoas'
         return math.ceil(pessoas/capacidade)