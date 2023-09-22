def concatenacao(a,b):
    '''Esta função utiliza duas strings e concatena ambas no formato abba
    assinatura: str, str -> str
    testes:
    concatenacao('bom','dia')='bomdiadiabom'
    concatenacao('passei','cálculo')='passeicálculocálculopassei'
    concatenacao('24h','programando')='24hprogramandoprogramando24h'
    '''
    return (a+b)+(b[::1]+a[::1])