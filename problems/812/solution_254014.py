def retira_pontuacao(frase):
    ''' função que retira a pontuação da frase'''
    str.replace(frase, ',', ' ')
    str.replace(frase,'-',' ')
    str.replace(frase,':',' ')
    str.replace(frase,';',' ')
    str.replace(frase,'.',' ')
    str.replace(frase,'!',' ')
    str.replace(frase,'?',' ')
    return frase