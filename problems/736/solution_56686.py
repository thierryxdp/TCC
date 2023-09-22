def concatenacao(a,b):
    '''Esta função utiliza duas strings e concatena ambas no formato abba
    assinatura: str, str -> str
    testes:
    '''
    return (a+b)+(b[::-1]+a[::-1])