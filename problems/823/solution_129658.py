def faltante(lista):
    list.sort(lista)
    n = 0 
    numero = 0
    while n < len(lista):
        if lista[n-1] != (int(lista[n]) - 1):
            numero = numero + n
        n = n+1
    return numero