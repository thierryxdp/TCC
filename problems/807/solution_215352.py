def conta_frases(frase):
    '''calcula quantas frases exitem em um dado texto
    str->int'''
    s=frase
    t1=len(s.split('.'))
    t2=s.len(s.split('?'))
    t3=s.len(s.split('...'))
    t4=s.len(s.split('!'))
    return t1+t2+t3+t4