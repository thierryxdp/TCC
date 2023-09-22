def retira_pontuacao (frase):
    '''Função que substitui a pontuação da frase por espaço.
    str->str'''
    frase1 = str.replace(frase, ' ', ',')
    frase2 = str.replace(frase, '...', ' ')
    frase3 = str.replace(frase, ' ', '.')
    frase4 = str.replace(frase, '!', ' ')
    frase5 = str.replace(frase, '?', ' ')
    frase6 = str.replace(frase, '-', ' ')
    frase7 = str.replace(frase, ':', ' ')
    frase8 = str.replace(frase, ';', ' ')
    
    return frase