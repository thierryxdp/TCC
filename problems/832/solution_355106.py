def eh_quadrada(m):
    '''
    Verifica se uma matriz e quadrada ou nao.
    
    Entrada/Saida:
    list -> bool
    '''
    if m == []:
        return None
    return len(m) == len(m[0])