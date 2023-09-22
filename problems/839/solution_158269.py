def carros (pessoas, capacidade=5):
        '''Definir a quantidade carros necessária para transportar um grupo de pessoas respeitando o limite de 5'''
        if pessoas == 0:
                return (0)
        if pessoas >= 1 and pessoas <= 5 :
                return (pessoas==1// capacidade==1)
        if pessoas >= 6 and pessoas <= 10:
                return (pessoas==1// capacidade==1)+1
        if pessoas >=11 and pessoas <= 14:
                return (pessoas==1// capacidade==1)+2
        if pessoas >=16 and pessoas <= 20 :
                return (pessoas==1// capacidade==1)+3