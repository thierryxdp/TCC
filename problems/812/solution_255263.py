def retira_pontuação(frase):
    ''' funcao que dada uma frase retira os caracteres
    '''
    caracteres ="!-,.@#?"
    for caracteres in ' ':
        frase = frase.split(caracteres,"")
    return frase