def retira_pontuacao(frase):
    a=str.replace(frase,'.',' ')
    b=str.replace(a,',',' ')
    c=str.replace(b,'!',' ')
    d=str.replace(c,'?',' ')
    e=str.replace(d,'-',' ')
    f=str.replace(e,':',' ')
    g=str.replace(f,';',' ')
    return g

def inverte(frase):
    a=retira_pontuacao(frase)
    b=str.lower(a)
    c=str.split(b,' ')
    d=c[::-1]
    e=str.join(' ',d)
    return str.strip(e)