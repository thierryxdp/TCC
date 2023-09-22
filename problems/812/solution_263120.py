def retira_pontuacao(frase):
    '''troca qualquer pontuacao da frase por  espaco
    str --> str'''
    str.replace(frase,'.',' ')
    str.replace(frase,',',' ')
    str.replace(frase,':',' ')
    str.replace(frase,'-',' ')
    return frase