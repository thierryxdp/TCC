def inverte(frase):
    '''função responsável por inverter uma frase, (frase), da escolha do usuário'''
    x=frase.replace('.',' ')
    y=x.replace('!',' ')
    w=y.replace('?',' ')
    z=w.replace('-',' ')
    a=z.replace(',',' ')
    b=a.replace(':',' ')
    c=b.replace(';',' ')
    d=c.split()
    e=d[::-1]
    f=' '.join(e)
    g=f.lower()
    return g