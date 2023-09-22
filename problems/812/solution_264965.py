def pontuação(x):
    a=str.replace(x,'.',' ')
    b=str.replace(a,':',' ')
    c=str.replace(b,';',' ')
    d=str.replace(c,',',' ')
    e=str.replace(d,'—',' ')
    return e