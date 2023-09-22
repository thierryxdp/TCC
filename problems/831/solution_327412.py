def lingua_p(palavra):
    lista = list(palavra)
    for x in lista:
        if x in 'aeiou':
            palavra.replace(x, x + 'p' + x)
    return palavra