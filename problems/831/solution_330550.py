def lingua_p(palavra):
    lista = list(palavra)
    lista1 = lista
    n = 0
    while n < len(lista):
        if lista[n] in "aeiou":
            list.insert(lista1, n + 1, 'p')
            list.insert(lista1, n + 2, lista[n])
        n = n + 1    
    return sum(lista1)