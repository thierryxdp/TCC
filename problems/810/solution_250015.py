def inversa(x):
    'Função que remove a pontuação e inverte a ordem de uma frase.'
    'str->str'
    a=str.replace(x,'.',' ')
    b=str.replace(a,':',' ')
    c=str.replace(b,';',' ')
    d=str.replace(c,',',' ')
    e=str.replace(d,'—',' ')
    f=str.lower(e)
    g=str.split(f)
    list.reverse(g)
    h=str.join(' ',g)
    
    return h