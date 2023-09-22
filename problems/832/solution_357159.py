def eh_quadrada(m):
    '''Escreva uma matriz. A funcao identifica se a matriz e quadrada
    e retorna um booleano (True ou False).
    list -> bool'''
    if (type(m)==list and len(m)==0) or (len(m)==0 or len(m)==len(m[0])):
        return True
    else:
        return False