def carros(passageiros, capacidade=5):
    ''' Essa função calcula quantos veiculos são necessarios para transportar quantidades de passageiros diferentes, usando veiculos de capacidade padão ou não '''
  
    import math
    return math.ceil(passageiros/capacidade)