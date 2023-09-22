def retira_pontuacao(frase):
    '''Função que retira a pontuação de um dada frase
    str -> str'''
    a = str.replace(frase, '-', ' ')
    b = str.replace(frase, ',', ' ')
    c = str.replace(frase, ':', ' ')
    d = str.replace(frase, ';', ' ')
    e = str.replace(frase, '...', ' ')
    f = str.replace(frase, '.', ' ')
    g = str.replace(frase, '!', ' ')
    h = str.replace(frase, '?', ' ')
    return h