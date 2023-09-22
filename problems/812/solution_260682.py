def retira_pontuacao(frase):
    '''Dada uma frase, substitui todos os caracteres de
    pontuação por espaço
    str -> str'''
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, '-', ' ')
    return frase