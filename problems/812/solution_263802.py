def retira_pontucao(frase):
    ''' Esta função retira as pontuções, colocando ponto no lugar.
    str->str'''
    frase_nova = str.replace(frase,'.',' ')
    frase_nova = str.replace(frase,',',' ')
    frase_nova = str.replace(frase,';',' ')
    frase_nova = str.replace(frase,':',' ')
    frase_nova = str.replace(frase,'?',' ')
    frase_nova = str.replace(frase,'!',' ')
    return frase_nova