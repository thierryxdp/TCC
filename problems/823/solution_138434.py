def faltante(lista):
    lista.sort()
    anterior = -1
    for n in lista:
        if(n - anterior == 1):
            anterior = n
        else:
            return n-1