def lingua_p(palavra):
    '''Recebe uma palavra e retorna a mesma palavra traduzida para a
    lingua do P.

    str -> str'''

    palavra = str.lower(palavra)

    vogais = 'aeiouáéíóúâêôãõ'

    palavraLinguaP = ''

    for indice in palavra:
        if indice in vogais:
            palavraLinguaP = palavraLinguaP + indice + 'p' + indice
        else:
            palavraLinguaP = palavraLinguaP + indice

    return palavraLinguaP