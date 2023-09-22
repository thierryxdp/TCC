def carros (num_pessoas, capacidade=5):
    '''função retorna o numero necessário de carros capazes de transportar as pessoas
    	que deseja (num_pessoas) porem os veículos devem obdecer a capacidade de até
        5 passageiros capacidade<=5'''
    if num_pessoas>=capacidade:
        return num_pessoas//capacidade
    elif num_pessoas<capacidade:
        return 1