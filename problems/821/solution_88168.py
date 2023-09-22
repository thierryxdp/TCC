def fatorial(n):
    """
    
    """
    lista_AntecessoresN = list(range(1, n + 1))
    N_fatorial = 1
    i = 0
    
    while i < len(lista_AntecessoresN):
        if lista_AntecessoresN[i] > 0:
            N_fatorial = Nfatorial * lista_AntecessoresN[i]
        i = i+1  
    return N_fatorial