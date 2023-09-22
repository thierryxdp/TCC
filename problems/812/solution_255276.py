def retira_pontuacao(frase):
    ''' funcao que dada uma frase retira os caracteres
    '''
    for caracteres in "-,:;,.~^*&¨%$#@?!":
        frase = frase.replace(caracteres," ")
    return frase