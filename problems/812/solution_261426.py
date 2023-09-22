def retira_pontuacao(frase):
    a=str.replace(frase,'-',' ')
    b=str.replace(a,':',' ')
    c=str.replace(b,',',' ')
    d=str.replace(c,';',' ')
    e=str.replace(d,'.',' ')
    return e