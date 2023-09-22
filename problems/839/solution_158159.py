def carros (pessoas, capacidade=5):
        '''Definir a quantidade carros necessária para transportar um grupo de pessoas respeitando o limite de 5 '''
        if pessoas and pessoas < 1 :
            return (pessoas * capacidade)
        if pessoas > 1 and pessoas < 5 :
            return (1)
        if pessoas > 5 and pessoas < 10 :
                return (2)
        if pessoas > 10 and pessoas < 14 :
                return (3)
        if pessoas > 14 and pessoas < 19 :
                return (4)