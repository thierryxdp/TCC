def conta_frases ("texto")
    p1=texto.count('.')
    p2=texto.count('!')
    p3=texto.count('?')
    p4=texto.count('...')
    if  p4!=0:
        return p1-(3*p4)+p2+p3+p4
    return p1+p2+p3+p4