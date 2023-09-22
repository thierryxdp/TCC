def tira_pontuacao(sentenca):
    a=str.replace(sentenca,'-',' ')
    b=str.replace(a,',',' ')
    c=str.replace(b,';',' ')
    d=str.replace(c,':',' ')
    e=str.replace(d,'...',' ')
    f=str.replace(e,'?',' ')
    g=str.replace(f,'!',' ')
    h=str.replace(g,'.',' ')
    return str.lower(h)
def inverte(frase):
    i=tira_pontuacao(frase)
    str.replace(i,'  ',' ')
    j=str.split(i,' ')
    list.remove(j,'')
    list.reverse(j)
    if frase[-1]=='.':
        k=str.join(' ',j)
        return k[1:-1]
    else:
        return str.join(' ',j)