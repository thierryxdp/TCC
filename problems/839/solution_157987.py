def carros (pessoas, capacidade):
        '''Definir a quantidade carros necessária para transportar um grupo de pessoas respeitando o limite de 5 '''
        if pessoas < capacidade:
                return (1)        
        if pessoas > 1 and capacidade < 5 :
                return (pessoas// capacidade)
        if pessoas < 6:
                return (pessoas// capacidade)
        if pessoas > 5:
                return (pessoas// capacidade + 1)