def faltante(lista):
    
    y = 0
    if lista[y] == y + 1:
        while lista[y] == y + 1:
            y = y + 1
        return y
    elif lista[y] == 0:
        return y + 1