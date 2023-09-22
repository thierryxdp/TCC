def lingua_p(palavra):
    minusculo = palavra.lower()
    nova_palavra = ''
    vogais = 'aeiouãéíóú'
    for p in range(0, len(palavra)):
        if minusculo[p] in vogais:
            nova_palavra += minusculo[p]

        else:
            nova_palavra += minusculo[p] + 'p'

    return nova_palavra