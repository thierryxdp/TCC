def retira_pontuacao(frase):
    '''funcão que dado uma frase, retorne a frase onde todos os caracteres de
    pontuação tenha sido substituidos poe espaço'''
    frase = str.replace(',',' ')
    frase = str.replace('.',' ')
    frase = str.replace(':',' ')
    frase = str.replace(';',' ')
    frase = str.replace('^',' ')
    frase = str.replace('~',' ')
    frase = str.replace('´',' ')
    frase = str.replace('`',' ')
    frase = str.replace('!',' ')
    frase = str.replace('?',' ')
    frase = str.replace('/',' ')
    frase = str.replace('-',' ')
    frase = str.replace('_',' ')
    frase = str.replace('\',' ')
                       return frase