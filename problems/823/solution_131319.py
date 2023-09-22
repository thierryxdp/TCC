def faltante(lista):

    list.sort(lista)
    i=0
    
    while i < len(lista):
        if lista[0] != 1:
            return 1

        elif lista[i] - lista[i - 1] != 1 and i > 0:
            return lista[i] - 1

        i += 1
        
    return lista[i] + 1