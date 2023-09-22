def qtd_divisores(n):
    '''Retorna quantos divisores o numero n possui'''
    resposta=0
    for divisor in range(n):
        if divisor!=0 and n%divisor==0:
            resposta=resposta+1
    return resposta