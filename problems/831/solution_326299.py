def lingua_p(palavra):
    """ddsfmndsj"""
    palavra = list(palavra.lower())
    i = 0
    for x in palavra:
        if x in 'aãaéeiou':
            soma = 'p'+x
            palavra.insert(palavra.index(x, i)+1, soma)
        i += 1
    copia = ''.join(palavra)
    return copia