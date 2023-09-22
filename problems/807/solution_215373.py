def conta_frases(frase):
    '''calcula quantas frases exitem em um dado texto
    str->int'''
    s=frase
    t1=s.split('.')
   	t2=s.split('?')

    return t1+t2