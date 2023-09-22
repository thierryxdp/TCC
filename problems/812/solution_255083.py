def retira_pontuacao(frase):
    ''' funcao que dada uma frase retira os caracteres
    '''
    frase_ = str.rstrip(str.lstrip(frase))
    return str.join('',frase)