def retira_pontuacao(m):
    a=str.replace(m,'-',' ')
    b=str.replace(a,'.',' ')
    c=str.replace(b,':',' ')
    d=str.replace(c,';',' ')
    e=str.replace(d,'!',' ')
    f=str.replace(e,'?',' ')
    g=str.replace(f,',',' ')
    h=str.replace(g,'/',' ')
    return h

def inverte(f):
    s=str.split(f)
    list.reverse(s)
    str.join('.',s)
    return retira_pontuacao(s)