def qtd_divisores(n):
    """ dado um numero, calcula e retorna a quantidade de
    divisores que ele tem;
    int -> int"""
    resposta = 0
    for numero in range(1, n+1):
        if n % numero == 0:
            resposta += 1
    return resposta