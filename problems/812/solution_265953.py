def retira_pontuacao (frase):
    '''Função que substitui a pontuação da frase por espaço.
    str->str''' 
    frase1 = frase.replace(',', ' ')
    frase2 = frase.replace('...', ' ')
    frase3 = frase.replace('.', ' ')
    frase4 = frase.replace('!', ' ')
    frase5 = frase.replace('?', ' ')
    frase6 = frase.replace('-', ' ')
    frase7 = frase.replace(':', ' ')
    frase8 = frase.replace(';', ' ')    
    return frase