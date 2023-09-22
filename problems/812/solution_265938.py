def retira_pontuacao (texto):
    '''Função que substitui a pontuação de um texto por espaço.
    str->str'''
    frase1 = str.replace(texto, ",", " ")
    frase2 = str.replace(texto, "...", " ")
    frase3 = str.replace(texto, ".", " ")
    frase4 = str.replace(texto, "!", " ")
    frase5 = str.replace(texto, "?", " ")
    frase6 = str.replace(texto, "-", " ")
    frase7 = str.replace(texto, ":", " ")
    frase8 = str.replace(texto, ";", " ")
    
    return texto