def fatorial(x):
    """Funcao que retorna o fatorial de um número dado
    int->inst"""
    resposta=1
    num=2
    while num<=x:
        resposta = resposta*num
        num=num+1
    return resposta