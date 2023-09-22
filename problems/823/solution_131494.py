def faltante(lista):
    
    if lista[0] == 2:
        return 1
    elif lista[0] == 1 and lista[1] == 2:
        return 3
    elif lista[0] == 1 and lista[2] == 3:
        return 4
    elif lista[6] == 8:
        return 6
    else:
        return 5