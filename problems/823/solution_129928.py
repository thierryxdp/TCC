def faltante (lista):
    
    list.sort (lista)
    i=0
    
    if lista [0] != 1 :
        return 1
    while i < len (lista) - 1 :
        if lista [i] + 1 != lista [ i + 1 ] :
            return lista[i] + 1
        i = i + 1
        return lista [-1] + 1