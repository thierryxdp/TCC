def repetidos(lista):
    n = 0
    vezes = 0
    maisum = lista[n+1]
    while n <= ((len(lista))-1):
        if lista[n] == lista[maisum]:
            vezes = vezes + 1
            n = n + 1
        elif lista[n] != lista2:
                n = n + 1
                
    return vezes