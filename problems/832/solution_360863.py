def eh_quadrada(m):
    """dado uma matriz, retorna true se for uma matriz quadrada
    e false para caso nao seja.
    list-->bool"""
    numeroLinhas=len(m)
    if len(m)==0:
        return True 
    else:
        numeroColunas=len(m[0])
        if numeroColunas==numeroLinhas:
            return True
        else:
            return False