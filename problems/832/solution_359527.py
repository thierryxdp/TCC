def eh_quadrada(n):
    '''Dado uma matriz(n), identifica se esta é uma matriz quadrada. list(list)-> boolean'''
    if n==[]:
        return True
    if len(n)==len(n[0]):
        return True
    else:
        return False