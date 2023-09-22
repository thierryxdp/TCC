n=2
def eh_quadrada(n):
    '''Funcao que diz se a matriz e quadrada ou nao'''
    '''list -> bool'''
    matriz =[] 
    for i in range(n):
        linha =[] 
        for j in range(n):
            matriz.append(linha)
    if i == j:
        return True
    else:
        return False