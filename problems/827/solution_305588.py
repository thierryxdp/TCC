def qtd_divisores(n):
    x = list(range(n))[1:]
    resultado = 0
    for i in x:
        if n%x[i]==0:
            resultado = resultado + 1
    return resultado