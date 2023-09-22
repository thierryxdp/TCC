def qtd_divisores(n):
    '''Funcao que retorna quantos divisores comuns
    o numero inserido possui
    '''
    r = 0
    for x in range(1,n+1):
        if n % x == 0:
            r += 1
    return r