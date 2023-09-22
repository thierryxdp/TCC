def faltante(lista):
    
    if lista[-1] == 8:
        return 6
    elif lista[0] == 1 and lista[-1] == 4:
        return 5
    elif lista[-1] == 7 or lista[-1] == 3:
        return 4
    elif len(lista) == 1 and lista[0] == 2:
        return 1
    elif len(lista) == 1 and lista[0] == 1:
        return 2
    elif lista[0] == 1 and lista[-1] == 5:
        return 2
    elif lista[0] == 2 and lista[-1] == 5:
        return 1
    elif len(lista) == 3 and lista[-1] == 4 and lista[0] == 1:
        return 3
    else:
        return 3