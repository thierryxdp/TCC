def qtd_divisores(x):
    """A funçao conta quantos divisores tem o numero x de entrada.int-->int"""
    contagem = 0
    for i in range(1,x+1):
        if x % i == 0:
            contagem = contagem + 1
    return contagem