def conta_frases(a):
    '''dada uma string, é informado quantas frases tem nela
       str -> int'''
    b1=str.count(a,'...')
    if b1>0:
        b=str.strip(a,'...')
    c1=str.count(b,'.')
    if c1>0:
        c=str.strip(b,'.')
    d1=str.count(c,'!')
    if d1>0:
        d=str.strip(c,'!')
    e1=str.count(d,'?')
    if e1>0:
        e=str.strip(d,'?')
    
    return b1+c1+d1+e1