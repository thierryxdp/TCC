def total(lista, dicionario):
    y = 0
    x = 0
    for x in range(len(dicionario)):
        a = lista[x]
        c = dict.get(dicionario, dicionario[a])
    y = y + c        
    x = x + 1   
    return c