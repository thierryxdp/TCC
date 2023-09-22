def retira_pontuacao(frase):
    '''Função que retira a pontuação de uma frase'''
    str.replace(frase,'.',' ')
    str.replace(frase,',',' ')
    str.replace(frase,':',' ')
    str.replace(frase,'-',' ')
    str.replace(frase,';',' ')
    str.replace(frase,'!',' ')
    str.replace(frase,'?',' ')
    str.replace(frase,'.',' ')