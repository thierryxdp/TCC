def retira_pontuacao(frase):
    ''' funcao que dada uma frase retira os caracteres
    '''
    for char in ".,!@#$%¨&*?;:~^´`/çãé":
        frase = frase.replace(char,"")
    return frase