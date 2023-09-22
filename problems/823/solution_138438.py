def faltante(lista):
    lista.sort()
    anterior = -1
    for n in lista:
        if(lista[0] > 1):
            return n-1
            
        if(lista[-1] == n):
            return n+1