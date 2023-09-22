def qntd_divisores(n):
    resultado = 0
    for divisores in range((1), n+1):
        if n % divisores == 0:
            resultado += 1
    return resultado