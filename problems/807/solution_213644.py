def conta_frases(texto):
    """retorna o número de frases do texto. Cada frase é terminada com um ponto final, um ponto de exclamação, um ponto de interrogação ou reticências
    str->int"""
    x=str.count(texto,'...')
    y=str.count(texto,'!')
    z=str.count(texto,'?')
    w=str.count(texto,'.')
    p=3*x
    q=x-p
    return(y+z+w+q)