def retira_pontucao(frase):
    ''' Esta função retira as pontuções, colocando ponto no lugar.
    str->str'''
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'!',' ')
    return frase