def retira_pontuacao (texto):
    '''Função que substitui a pontuação de um texto por espaço.
    str->str'''
    frase = texto
    frase1 = str.replace(frase, ",", " ")
    frase2 = str.replace(frase, "...", " ")
    frase3 = str.replace(frase, ".", " ")
    frase4 = str.replace(frase, "!", " ")
    frase5 = str.replace(frase, "?", " ")
    frase6 = str.replace(frase, "-", " ")
    frase7 = str.replace(frase, ":", " ")
    frase8 = str.replace(frase, ";", " ")
    
    return frase