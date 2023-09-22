def faltante(lista):
    lista = list.sort(lista)
    i = 1
    while i < len(lista):
        if i == lista[i - 1]:
            k += 1
        i += 1
    
    return k