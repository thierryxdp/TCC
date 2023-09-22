def repetidos(lista):
    n = 0
    vezes = 0
    lista2 = lista[n+1]
    while n <= len(lista):
        if lista[n] == lista2:
            vezes = vezes + 1
            n = n + 1
        elif lista[n] != lista2:
                n = n + 1
                
    return vezes