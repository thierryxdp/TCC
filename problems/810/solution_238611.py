def inverte(frase):
    s=frase
    f1=s.split('!')
    f2=str.join(' ',f1)
    f3=f2.split('.')
    f4=str.join(' ',f3)
    f5=f4.split(',')
    f6=str.join(' ',f5)
    f7=f6.split('-')
    f8=str.join(' ',f7)
    f9=f8.split('?')
    f10=str.join(' ',f9)
    m=f10.split(' ')
    r=m[0]
    t=len(m)
    k=r[-1:-t-1:-1]
    d=str.join(' ',k)
    return str.lower(d)