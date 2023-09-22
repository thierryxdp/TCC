def concatenacao(a,b):
    '''Esta função utiliza duas strings e concatena ambas no formato abba
    assinatura: str, str -> str
    testes:
    '''
    return (a+b)+(a[::-1]+b[::-1])