def carros (pessoas, capacidade=5):
        '''Definir a quantidade carros necessária para transportar um grupo de pessoas respeitando o limite de 5 '''
        if pessoas or capacidade < 1:
		        return (0)
        if pessoas < capacidade:
                return (1)        
        if pessoas > 1 and capacidade < 4 :
                return (pessoas// capacidade)
        if pessoas < 6:
                return (pessoas// capacidade)
        if pessoas > 5:
                return (pessoas// capacidade + 1)