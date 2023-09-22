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
        if pessoas >= 11 and pessoas <= 15 :
                import math
                return math.ceil((pessoas/   capacidade))
        if pessoas >= 11 and pessoas <= 15 and capacidade >= 11 and capacidade <= 15 :
                import math
                return math.ceil((pessoas/ capacidade))
        if pessoas >= 16 and pessoas <= 20 :
                import math
                return math.ceil((pessoas/   capacidade))
        if pessoas >= 16 and pessoas <= 20 and capacidade >= 16 and capacidade <= 20 :
                import math
                return math.ceil((pessoas/ capacidade))