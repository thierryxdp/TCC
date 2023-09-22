def eh_quadrada(a):
    ''' funcao identifica se a matriz é ou não quadrada
    int -> int'''
    matriz = []
    b = 0
    for i in a:
        b = len(i)
    if len(a) == b:
        return(True)
    elif len(a) == matriz:
        return(True)
    else:
        return(False)