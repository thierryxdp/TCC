def inverte(x):
    'Função que remove a pontuação e inverte a ordem de uma frase.'
    'str->str'
    a=str.replace(x,'.',' ')
    b=str.replace(a,':',' ')
    c=str.replace(b,';',' ')
    d=str.replace(c,',',' ')
    e=str.replace(d,'—',' ')
    f=str.replace(e,'?',' ')
    g=str.replace(f,'!',' ')
    h=str.replace(g,'-',' ')
    i=str.lower(h)
    j=str.split(i)
    list.reverse(j)
    k=str.join(' ',j)
    
    return k