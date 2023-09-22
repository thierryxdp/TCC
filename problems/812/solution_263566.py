def retira_pontuacao(frase):
    for frase != '':
        str.replace(frase,'-',' ')
        str.replace(frase,',',' ')
        str.replace(frase,':',' ')
        str.replace(frase,';',' ')
        str.replace(frase,'.',' ')
        str.replace(frase,'...',' ')
        str.replace(frase,'!',' ')
        str.replace(frase,'?',' ')
        return frase