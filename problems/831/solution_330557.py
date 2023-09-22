def lingua_p(palavra):
    lista = list(palavra)
    lista1 = lista.copy()
    n = 0
    for n in range(len(lista)):
        if lista[n] in "aeiou":
            list.insert(lista1, n + 1, 'p')
            list.insert(lista1, n + 2, lista[n])
        n = n + 1    
    return lista1