def fatorial(n):
    '''Recebe um número e retorna o fatorial desse número; int->int'''
    proximo=1
    resposta=1
    while proximo<=n:
        resposta=resposta*proximo
        proximo=proximo+1
    return resposta