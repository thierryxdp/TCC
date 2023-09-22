def qtd_divisores(n):
    contador = 0
    acumulador = []
    for numero in list(range(n)):
        if n%(n-contador) == 0:
            acumulador = acumulador + [1]
        contador = contador + 1
    return len(acumulador)