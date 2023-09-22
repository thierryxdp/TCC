def carros (pessoas, capacidade):
        '''Definir a quantidade carros necessária para transportar um grupo de pessoas respeitando o limite de 5 '''
        if pessoas < 6:
                return (pessoas// capacidade)
        if pessoas > 5:
                return (pessoas// capacidade + 1)
        if pessoas < 1:
                return (capacidade - capacidade)
        if pessoas and capacidade:
                return (1 - 1)