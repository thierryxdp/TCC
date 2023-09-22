def filtra_pares(tupla):
    """funcao que dado de entrada um tupla com 4 elementos
    inteiros, retorna uma nova tupla contendo somente os 
    elementos pares da tupla original;
    tuple -> tuple"""
    
    for elem in tupla:
        if elem%2 == 0:
            return append(elem)
        else:
            return tuple()