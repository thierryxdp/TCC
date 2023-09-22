def soma_h(numero):
    """Função que calcula o H com numero indicado.
    Parametro: int->float"""
    soma = 0
    for i in range(1, numero + 1):
        divisao = (1/i)
        soma += divisao
    return round(soma, 2)