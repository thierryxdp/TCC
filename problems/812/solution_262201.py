def retira_pontuacao(frase):
    '''substitui os caracteres de pontuacao por espaco'''
    #str -> str
    return str.replace(frase, '—', ' ')
    str.replace(frase, ',', ' ')
    str.replace(frase, ':', ' ')
    str.replace(frase, ';', ' ')
    str.replace(frase, '.', ' ')