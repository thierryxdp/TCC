def filtra_pares(elementos):
    '''Função que recebe uma tupla e retorna os elementos 
    pares dessa mesma
    valor de entrada: tuple
    valor de saída: tuple '''
    e1,e2,e3,e4= elementos
    if e1%2==0:
        return tuple(e1)
    elif e2%2==0:
        return tuple(e2)
    elif e3%2==0:
        return tuple(e3)
    elif e4%2==0:
        return tuple(e4)