def carros (pessoas, capacidade=5):
        '''Definir a quantidade carros necessária para transportar um grupo de pessoas respeitando o limite de 5'''
        if pessoas == 0:
                return (0)
        if pessoas >= 1 and pessoas <= 5:
                return (1)
        if pessoas >= 5 and pessoas <= 10:
                return (2)
        if pessoas >=11 and pessoas <= 15:
                return round(pessoas// capacidade + 1)
        if pessoas >=16 and pessoas <= 20 :
                return round(4)