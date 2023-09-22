def retira_pontuacao(frase):
    '''troca qualquer pontuacao da frase por  espaco
    str --> str'''
    frase1 = str.replace(frase,'.',' ')
    frase2 = str.replace(frase1,',',' ')
    frase3 = str.replace(frase2,':',' ')
    frase4 = str.replace(frase3,'-',' ')
    return frase4