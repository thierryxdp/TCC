def retira_pontuacao (frase):
    '''Função que substitui a pontuação da frase por espaço.
    str->str'''
    frase1 = replace(frase, ",", " ")
    frase2 = replace(frase, "...", " ")
    frase3 = replace(frase, ".", " ")
    frase4 = replace(frase, "!", " ")
    frase5 = replace(frase, "?", " ")
    frase6 = replace(frase, "-", " ")
    frase7 = replace(frase, ":", " ")
    frase8 = replace(frase, ";", " ")
    
    return frase