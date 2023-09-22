def retira_pontuacao(a):
    f=str.replace(a,'-',' ',2)
    b=str.replace(f,',',' ',2)
    c=str.replace(b,':',' ',2)
    d=str.replace(c,';',' ',2)
    e=str.replace(d,'.',' ',2)
    g=str.replace(e,'!',' ',2)
    h=str.replace(g,'?',' ',2)

def inverte(a):
    retira_pontuacao(a)
    i=str.split(h,' ')
    j=reversed(i)
    k=str.join(j)
    return k