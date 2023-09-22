def eh_quadrada(m):
    '''
    Verifica se uma matriz e quadrada.
    
    Entrada/Saida:
    list -> bool
    '''
    if m == []:
		return True
    return len(m) == len(m[0])