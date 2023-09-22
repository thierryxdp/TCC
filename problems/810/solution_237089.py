def inverte(frase):
    x=frase.split(' ')
    w=x.split('.')
    t=w.split(',')
    h=t.split('?')
    i=h.split('!')
    a=i.split('-')
    y=a[::-1]
    z=str.join(' ',a)
    return z