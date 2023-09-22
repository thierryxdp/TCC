def lingua_p(frase):

    for dado in '''aeiouáéíóú''':

        frase = frase.replace(dado, dado + 'p' + dado)

    return frase