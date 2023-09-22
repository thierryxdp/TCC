def tira_pontuacao(sentenca):
    a=str.replace(sentenca,'-','')
    b=str.replace(a,',','')
    c=str.replace(b,';','')
    d=str.replace(c,':','')
    e=str.replace(d,'...','')
    f=str.replace(e,'?','')
    g=str.replace(f,'!','')
    h=str.replace(g,'.','')
    return str.lower(h)
def inverte(frase):
    i=tira_pontuacao(frase)
    j=str.split(i,' ')
    list.reverse(j)
    k=str.join(' ',j)
    return k