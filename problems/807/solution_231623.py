def conta_frases(texto):
    '''A função retorna o número de frases contidas em um
    texto. Entende-se por frase, um trecho do texto terminado 
    em ponto final, ponto de interrogação, exclamação 
    ou reticências. str -> int'''
    a=texto.split('!')
    b='.'.join(a)
    c=b.split('?')
    d='.'.join(c)
    e=d.split('...')
    f='.'.join(e)
    g=f.split('.')
    return len(g)-1