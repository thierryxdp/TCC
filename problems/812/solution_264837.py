def retira_pontuacao(frase):
    '''função que dada uma frase, substitui todos os caracteres de pontuação por espaço'''
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '...', ' ')
    frase = str.replace(frase, ':', ' ')
    return frase