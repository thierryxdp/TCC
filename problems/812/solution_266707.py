def retira_pontuacao(frase):
    '''função que recebe uma frase e retorna os caracteres de pontuação por espaço'''
    frase = frase.replace(';',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace('.',' ')
    return frase