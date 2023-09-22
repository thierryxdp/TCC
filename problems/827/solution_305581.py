def qtd_divisores(n):
    x = list(range(n)):
    resultado = 0
    for i in x:
        if n[i]%n==0:
            resultado = resultado + 1
    return resultado