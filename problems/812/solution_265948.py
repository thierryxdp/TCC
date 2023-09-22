def retira_pontuacao (frase):
    '''Função que substitui a pontuação da frase por espaço.
    str->str'''
    frase1, frase2, frase3, frase4, frase5, frase6, frase7, frase8 = frase
    frase1 = str.replace(',', ' ')
    frase2 = str.replace('...', ' ')
    frase3 = str.replace('.', ' ')
    frase4 = str.replace('!', ' ')
    frase5 = str.replace('?', ' ')
    frase6 = str.replace('-', ' ')
    frase7 = str.replace(':', ' ')
    frase8 = str.replace(';', ' ')
    
    return frase