#->float
def soma_h(n):
    "Fução que calcula a soma de um inteiro fatorial e retorna o resultado com 2 casas decimais."
    soma = 0
    for x in range(1, n + 1):
        inverso = (1/x)
        soma += inverso
    return round(soma, 2)