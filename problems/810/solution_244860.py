def inverte(f):
    s=str.split(f)
    list.reverse(s)
    d=str.join('.',s)
    a=str.replace(d,'-',' ')
    b=str.replace(a,'.',' ')
    c=str.replace(b,':',' ')
    d=str.replace(c,';',' ')
    e=str.replace(d,'!',' ')
    f=str.replace(e,'?',' ')
    g=str.replace(f,',',' ')
    h=str.replace(g,'/',' ')
    return h