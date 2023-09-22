def retira_pontuacao(frase):
    ''' retira todos os caracteres de pontuação de uma frase 
    e os substitui por espaços;
    str->str'''
    frase=frase.replace(':',' ')
    frase=frase.replace(';',' ')
    frase=frase.replace(',',' ')
    frase=frase.replace('/',' ')
    frase=frase.replace('.',' ')
    frase=frase.replace('!',' ')
    frase=frase.replace('?',' ')
    return frase