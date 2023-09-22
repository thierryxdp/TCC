def eh_quadrada(m):
    '''funcao que identifica se uma matriz e quadrada'''
    numeroLinhas=len(m)
    if len(m)==0:
        return True 
    else:
        numeroColunas=len(m[0])
        if numeroColunas==numeroLinhas:
            return True
        else:
            return False