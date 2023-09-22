def maiores(lista,n):
    lista=list.sort(lista)
    resultado = []
    for i in range(len(lista)):
        if lista[i]>n:
            resultado.append(lista[i])

    return resultado