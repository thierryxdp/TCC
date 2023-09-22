def carros (pessoas, capacidade=5):
        '''Definir a quantidade carros necessária para transportar um grupo de pessoas respeitando o limite de 5'''
        if pessoas == 0:
                return (0)
        if pessoas >=1 and pessoas <= 5 :
                return round(pessoas// capacidade)
        if pessoas >=6 and pessoas <= 10:
                return (pessoas// capacidade)+1
        if pessoas >=11 and pessoas <= 14:
                return round(pessoas// capacidade)+2
        if pessoas >=15 and pessoas <= 20 :
                return round(pessoas// capacidade)+3