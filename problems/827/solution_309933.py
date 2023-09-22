def qtd_divisores(x):
    resultado = [for i in range(1 , x + 1) if x % i == 0]
    return resultado