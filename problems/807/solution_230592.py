def conta_frases(frase):
    '''função que conta o número de frases de um texto sendo
    que cada frase é terminada em: ponto de interrogação,
    ponto final, reticencias ou ponto de exclamação;
       str -> int'''
    f=frase
    return str.count(f,'!')+str.count(f,'...')+(str.count(f,'.')-3*str.count(f,'...'))+str.count(f,'?')