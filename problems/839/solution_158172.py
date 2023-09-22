def carros(p,c=5):
    '''Calcula o número de carros necessários para transportar
    um grupo de pessoas, dado uma quantidade de pessoas p e uma
    capacidade do veículo c.
    int, int -> int'''
    if p%c!=0:
        return p//c+1
    else:
    return p//c