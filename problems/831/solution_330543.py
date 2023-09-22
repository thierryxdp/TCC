def lingua_p(palavra):
    lista = list(palavra)
    n = 0
    while n < len(lista):
        if lista[n] in "aeiou":
            list.insert(lista, n + 1, 'p')
            list.insert(lista, n + 2, lista[n])
        n = n + 1    
    return sum(lista)