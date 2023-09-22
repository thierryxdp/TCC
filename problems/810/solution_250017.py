def inverte(x)
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
    list.reverse(h)
    i=str.join(' ',h)
    
    return i