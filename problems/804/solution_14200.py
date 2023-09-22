def filtra_pares(a,b,c,d):
    """ Função que recebe uma tupla contendo quatro elementos inteiros
    como parâmetro e retorna uma tupla contendo apenas os elementos pares
    na mesma ordem em que se encontravam.
    Entrada: Tupla
    Saída: Tupla
    """
    x=a%2
    y=b%2
    z=c%2
    w=d%2
    
    
    if x==0 and y==0 and z==0 and w==0:
        return a,b,c,d
    else:
        return None