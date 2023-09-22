def invert(frase):
    '''uhggu''''
    frase=retira_pontuacao(frase)
    palavras=frase.split(' ')
    palavras.remove('')
    palavras.reverse()
    return palavras