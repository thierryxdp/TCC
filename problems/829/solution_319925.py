def soma_h(n):
    """Funcao que retorna o fatorial de um número dado
    int->inst"""
    resposta=1
    soma=1
    num=2
    while num<=n:
        resposta = resposta/num
        num=num+1
        soma=soma+resposta
    return round(soma,2)