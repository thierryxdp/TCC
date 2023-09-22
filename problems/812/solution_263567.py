def retira_pontuacao(frase):
    for frase not '':
        str.replace(frase,'-',' ')
        str.replace(frase,',',' ')
        str.replace(frase,':',' ')
        str.replace(frase,';',' ')
        str.replace(frase,'.',' ')
        str.replace(frase,'...',' ')
        str.replace(frase,'!',' ')
        str.replace(frase,'?',' ')
        return frase