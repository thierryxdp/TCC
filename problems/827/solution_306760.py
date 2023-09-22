def qtd_divisores(n):
    '''Retorna os divisores do numero n possui'''
    resposta=[]
    for divisor in range(n):
        if divisor!=0 and n%divisor==0:
            resposta=resposta+divisor
    return resposta