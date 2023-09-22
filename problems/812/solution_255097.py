def retira_pontuacao(frase):
    ''' funcao que dada uma frase retira os caracteres
    '''
    caracteres== "-,:;,.~^*&¨%$#@!"
    frase = frase.replace(caracteres,"")
    return frase