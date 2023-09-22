def carros (pessoas, capacidade=5):
        '''Definir a quantidade de veiculos
para transportar uma certa quantidade de pessoas'''
        if pessoas == 0:
                return (0)
        if pessoas >= 1 and pessoas <= 5 and capacidade <= 5:
                import math
                return math.ceil(pessoas/ capacidade)
        if pessoas >= 6 and pessoas <= 10 :
                import math
                return math.floor((pessoas/   capacidade)* 2)
        if pessoas >= 6 and pessoas <= 10 and capacidade >= 6 and capacidade <= 10 :
                import math
                return math.floor((pessoas/ capacidade)* 2)