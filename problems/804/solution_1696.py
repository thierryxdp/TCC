def pares_impares(n1,n2,n3,n4):
    lista_valores = [n1,n2,n3,n4]
    lista_pares = []

    for contador in range(0, len(lista_valores)):
        if(lista_valores[contador]%2 == 0):
            lista_pares.append(lista_valores[contador])

    return lista_pares