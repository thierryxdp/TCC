def lingua_p(frase):

    for dado in '''aeiou''':

        frase = frase.replace(dado, dado + 'p')

    return frase