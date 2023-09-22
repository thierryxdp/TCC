def faltante(lista):
    lista1 = list(range(1,len(lista)+2))
    n = 0
    numero = 0
    while n < len(lista1):
        if lista1[n] not in lista:
            numero = numero + lista1[n]
        n = n+1
    return numero