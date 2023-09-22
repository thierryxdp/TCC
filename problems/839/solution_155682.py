from math import ceil

def carros(pessoas,capacidade=5):
    """
    calcula a quantidade exata de carros
    necessaria para realizar uma viagem
    dado o numero de pessoas. Caso 
    os carros comportem um numero diferente
    de pessoas do que 5, informar tambem
    a capacidade dos veiculos
    int,int--->int
    """
    
    p=pessoas
    c=capacidade
    
    return ceil(p/c)