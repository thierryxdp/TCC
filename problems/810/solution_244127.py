def retira_pontuacao(frase):
    a=str.replace(frase,',',' ')
    b=str.replace(a,'-',' ')
    c=str.replace(b,':',' ')
    d=str.replace(c,';',' ')
    e=str.replace(d,'...',' ')
    f=str.replace(e,'!',' ')
    g=str.replace(f,'?',' ')
    h=str.replace(g,'.',' ')
    return h

def inverte(frase):
    a=retira_pontuacao
    b=str.split(a)
    c=list.reverse(b)