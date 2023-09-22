def conta_frases(texto):
    '''função que dado um texto, retorna a quantidade de frases 
    presentes no texto; str-->int'''
    s=texto
    d=str.split(s,('!' and '?' and '.' and '...'))
    return len(d)