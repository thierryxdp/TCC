def qtd_divisores(n):
    resultado = 0
    for i in list(range(n)):
        if n[i]%n==0:
            resultado = resultado + 1
    return resultado