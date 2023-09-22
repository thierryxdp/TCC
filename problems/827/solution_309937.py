def qtd_divisores(x):
    contador = 0
    resultado = [i for i in range(1, x + 1) if x % i == 0]
    return resultado.count()