def inverte(frase):
    x=str.replace(frase,'.',' ')
    y=str.replace(x,',',' ')
    z=str.replace(y,':',' ')
    w=str.replace(z,';',' ')
    t=str.replace(w,'!',' ')
    u=str.replace(t,'?',' ')
    v=str.replace(u,'-',' ')
    h=v.split(' ')
    y=h[::-1]
    z=str.join(' ',y)
    i=z.lower()
    return i[1:]