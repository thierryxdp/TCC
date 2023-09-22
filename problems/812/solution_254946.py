def retira_pontuacao(frase):
    '''funcão que dado uma frase, retorne a frase onde todos os caracteres de
    pontuação tenha sido substituidos poe espaço
    str -> str'''
    frase = frase.replace(',',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('^',' ')
    frase = frase.replace('~',' ')
    frase = frase.replace('´',' ')
    frase = frase.replace('`',' ')
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('/',' ')
    frase = frase.replace('-',' ')
    frase = frase.replace('_',' ')
    return frase