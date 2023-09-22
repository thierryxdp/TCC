def fatorial(numero):
    '''funcao que retorna o fatorial de um numero'''
    i=numero
    resposta=i
    while i>0:
        resposta=resposta*(i-1)
        i=i-1
    return resposta