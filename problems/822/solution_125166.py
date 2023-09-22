def repetidos(lista):
    n = 0
    vezes = 0
    lista2 = lista[n+1]
    while n <= len(lista):
        if lista2 == lista[n+1]:
            vezes = vezes + 1
            n = n + 1
        elif lista2 != lista[n]:
                n = n + 1
                
    return vezes