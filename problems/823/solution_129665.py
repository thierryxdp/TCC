def faltante(lista):
    lista2 = lista[:-1]
    n = 0 
    numero = 0
    while n < len(lista2):
        if lista[n] != lista2[n]:
            numero = numero + lista[n]
        n = n+1
    return numero