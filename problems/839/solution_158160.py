def carros (pessoas, capacidade=5):
        '''Definir a quantidade carros necessária para transportar um grupo de pessoas respeitando o limite de 5 '''
        if capacidade and capacidade < 1 :
            return (pessoas * capacidade)
        if capacidade > 1 and capacidade < 5 :
            return (1)
        if capacidade > 5 and capacidade < 10 :
                return (2)
        if capacidade > 10 and capacidade < 14 :
                return (3)
        if capacidade > 14 and capacidade < 19 :
                return (4)