def faltante(lista):
    
    
    pecas = len(lista) + 1
    lista.sort()
    i = 0
    
    while i < pecas:
        if i + 1 not in lista:
            return i + 1
        elif lista[i] != i + 1:
            return i + 1
        else:
            i += 1
            return i