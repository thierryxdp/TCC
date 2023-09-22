def inverte(frase):
    '''funcao''''
    frase=retira_pontuacao(frase)
    palavras=frase.split(' ')
    palavras.remove('')
    palavras.reverse()
    return palavras