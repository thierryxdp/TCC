def faltante(lista):
    list.sort(lista)
    n = 0 
    numero = 0
    while n < (len(lista) -1):
        if lista[n] != lista[n+2]-1:
            numero = numero + n
        n = n+1
    return numero