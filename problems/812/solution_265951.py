def retira_pontuacao (frase):
    '''Função que substitui a pontuação da frase por espaço.
    str->str'''
    texto = frase
    
    frase1 = str.replace(texto, ',', ' ')
    frase2 = str.replace(texto, '...', ' ')
    frase3 = str.replace(texto, '.', ' ')
    frase4 = str.replace(texto, '!', ' ')
    frase5 = str.replace(texto, '?', ' ')
    frase6 = str.replace(texto, '-', ' ')
    frase7 = str.replace(texto, ':', ' ')
    frase8 = str.replace(texto, ';', ' ')
    
    return texto