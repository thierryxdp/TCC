def total(lista, dicionario):
    y = 0
    x = 0
    for numero in range(len(lista)):
        a = lista[x]
        c = dict.get(dicionario, a)
        y = y + c        
        x = x + 1   
    return round(y, 2)