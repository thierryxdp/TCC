def retira_pontuacao(f):
    x= str.replace(f,',',' ')
    y=str.replace(x,'-',' ')
    z=str.replace(y,':',' ')
    w=str.replace(z,'.',' ')
    e=str.replace(w,';',' ')
    t=str.replace(e,'!',' ')
    l=str.replace(t,'?',' ')
    return l
    
def inverte(f):
    m=str.lower(f)
    n=retira_pontuacao(m)
    p=list(n)
    o= p.reverse(p)
    return o