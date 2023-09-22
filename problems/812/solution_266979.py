def retira_pontuacao(frase):
    '''funação que retira a pontuação da frase'''
    f = frase
    f = str.replace(f,'!',' ')
    f = str.replace(f,'?',' ')
    f = str.replace(f,'.',' ')
    f = str.replace(f,',',' ')
    f = str.replace(f,';',' ')
    f = str.replace(f,'-',' ')
    return f