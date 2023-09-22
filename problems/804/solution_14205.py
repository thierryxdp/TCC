def filtra_pares(a,b,c,d):
    """ Função que recebe uma tupla contendo quatro elementos inteiros
    como parâmetro e retorna uma tupla contendo apenas os elementos pares
    na mesma ordem em que se encontravam.
    Entrada: Tupla
    Saída: Tupla
    """
    
    
    
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a, b, c, d)
    else:
        return (None)