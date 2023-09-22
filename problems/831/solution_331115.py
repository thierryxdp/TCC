def lingua_p(palavra):
    '''Adiciono uma letra p antes da vogal de uma dada palavra.
str --> str'''
    minusc= palavra.lower()
    nova_p = ''
    vogais = 'aeiouãéíóú'
    vogal_p = ''
    for x in range(0, len(palavra)):
        if minusc[p] in vogais:
            vogal_p += minusc[x]
            nova_p += minusc[x] + 'p' + vogal_p[:2]

        else:
            nova_p += minusc[x]
    vogais = 'aeiouãáéíóú'
    for x in minusc:
        nova_p += x
        if x in vogais:
            nova_p += 'p' + x

    return nova_palavra