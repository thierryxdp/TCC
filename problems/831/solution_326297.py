def lingua_p(palavra):
    """ddsfmndsj"""
    palavra = list(palavra.lower())
    i = 0
    for x in palavra:
        if x in 'aãaéiou':
            soma = 'p'+x
            palavra.append(palavra.index(x, i)+1, soma)
        i += 1
    copia = ''.join(palavra)
    return copia