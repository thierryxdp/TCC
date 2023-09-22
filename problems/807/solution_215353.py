def conta_frases(frase):
    '''calcula quantas frases exitem em um dado texto
    str->int'''
    s=frase
    t1=len(s.split('.'))
    t2=len(s.split('?'))
    t3=len(s.split('...'))
    t4=len(s.split('!'))
    return t1+t2+t3+t4