def maiores(lista_inteiros, n):
    resultado = []
    for i in range(len(lista_inteiros)):
        if lista_inteiros[i] > n:
            resultado.append(lista_inteiros[i])
    return resultado.sort()