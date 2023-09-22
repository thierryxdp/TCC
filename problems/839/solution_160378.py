def carros (num_pessoas, capacidade=5):
    '''função retorna o numero necessário de carros capazes de transportar as pessoas
    	que deseja (num_pessoas) e a capacidade do veículo caso seja convencional é igual a 5'''
    if num_pessoas>0:
        if num_pessoas>= capacidade:
            return num_pessoas//capacidade
        elif num_pessoas<capacidade:
            return 1
    else:
        return 0