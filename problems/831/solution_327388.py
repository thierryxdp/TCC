def lingua_p(palavra):
    lista = list(palavra)
    for x in lista:
        if x in 'aeiou':
            y = x.index
            'p'.insert(lista, y-1)
            'p'.insert(lista, y+1)
        return str(lista)