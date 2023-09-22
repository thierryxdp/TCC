def lingua_p(palavra):
    lista = list(palavra)
    n = 0
    for n in range(len(lista)):
        if lista[n] in "a":
            list.insert(lista, n + 1, 'pa')
        if lista[n] in "e":
            list.insert(lista, n + 1, 'pe')
        if lista[n] in "i":
            list.insert(lista, n + 1, 'pi')
        if lista[n] in "o":
            list.insert(lista, n + 1, 'po')
        if lista[n] in "u":
            list.insert(lista, n + 1, 'pu')
        n = n + 1    
    return sum(lista)