def retira_pontuacao(frase):
    ''' retira todos os caracteres de pontuação de uma frase 
    e os substitui por espaços;
    str->str'''
    frase.replace(':',' ')
    frase.replace(';',' ')
    frase.replace(',',' ')
    frase.replace('/',' ')
    frase.replace('.',' ')
    frase.replace('!',' ')
    frase.replace('?',' ')
    return frase