def retira_pontuacao(s):
    x=str.replace(s,'.',' ')
    y=str.replace(x,'!',' ')
    z=str.replace(y,'?',' ')
    c=str.replace(z,',',' ')
    v=str.replace(c,':',' ')
    b=str.replace(v,';',' ')
    n=str.replace(b,'-',' ')
    return n
def inverte(frase):
    x=retira_pontuacao(frase)
    y=str.split(x)
    z=y[:-1]
    return str.join(' ',z)