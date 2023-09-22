def maiores(lista,n):

    resultado = []
    for i in range(len(lista)):
        if lista[i]>n:
            resultado.append(lista[i])

    return resultado