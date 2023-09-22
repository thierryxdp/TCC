def retira_pontuacao (frase):
    '''funcao que retorna a frase onde todos os caracteres
    de pontuacao tenham sido substituidos por espaco'''
    '''str -> str'''
    frase = frase.replace('—',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace(';',' ')
    return frase