def retira_pontuacao(frase):
    '''substitui os caracteres de pontuacao por espaco'''
    #str -> str
    str.replace(frase, '—', ' ')
    str.replace(frase, ',', ' ')
    str.replace(frase, ':', ' ')
    str.replace(frase, ';', ' ')
    str.replace(frase, '.', ' ')
    return frase