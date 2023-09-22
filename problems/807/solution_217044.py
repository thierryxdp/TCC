def conta_frases(texto):
    '''função que dado um texto, retorna a quantidade de frases 
    presentes no texto; str-->int'''
    s=texto
    a=str.count(s,'!' and '?' and '.')
    b=str.count(s,'...')
    c=str.count(s,'...')*3
    return (a+b)-c