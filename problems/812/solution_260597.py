def retira_pontuacao(frase):
    '''Dado uma frase,substitui todos os caracteres de pontuação por espaço.str->str.'''
    frase1=(((frase.replace('.',' ').replace('!',' ')).replace(',',' ')).replace('-',' ')).replace('?',' ')
    return frase1