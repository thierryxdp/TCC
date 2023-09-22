def fatorial(num):
    """Função que dado um número calcula o fatorial deste número
    int -> int"""
    resposta = 1
    while num > 0:
        resposta = resposta * num
        num = num - 1
    return resposta