def retira_pontuacao(frase):
    a = frase
    a = str.replace(a,'...',' ')
    a = str.replace(a,',',' ')
    a = str.replace(a,'!',' ')
    a = str.replace(a,'.',' ')
    a = str.replace(a,'?',' ')
    a = str.replace(a,'—',' ')
    a = str.replace(a,':',' ')
    a = str.replace(a,';',' ')
    a = str.replace(a,'-',' ')
    return a