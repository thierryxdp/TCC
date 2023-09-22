def lingua_p(palavra):
    palavra = str.lower(palavra)
    lista = list(palavra)
    i = 0
    p = ''
    while i < len(lista):
        if lista[i] in 'aeiou':
            lista = lista[:i] + [lista[i]+'p'] + lista[i:]
            i += 3
        else:
            i += 1
    while i < len(lista):
        p = p + lista[i]
        i += 1
    return p