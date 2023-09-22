def eh_quadrada(m):
    '''Função com o objetivo de identificar se
    uma matriz é quadrada ou não.
    assinatura: matriz--> booleano
    '''
    numeroLinhas=len(m)
    if len(m)==0:
        return True 
    else:
        numeroColunas=len(m[0])
        if numeroColunas==numeroLinhas:
            return True
        else:
            return False