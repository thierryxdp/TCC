def conta_frases(a):
    '''dada uma string, é informado quantas frases tem nela
       str -> int'''
    b1=str.count(a,'...')
    b=str.strip(a,'...')
    c1=str.count(a,'.')
    c=str.strip(b,'.')
    d1=str.count(a,'!')
    d=str.strip(c,'!')
    e1=str.count(a,'?')
    e=str.strip(d,'?')
    
    return b1+c1+d1+e1