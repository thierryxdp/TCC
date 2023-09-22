def conta_frases(texto):
    """funçao que, dado um texto como entrada, retorna o numero de frases que esse texto contem, sendo elas delimitadas sempre por um ponto final, ponto de exclamaçao, ponto de interrogaçao ou reticencias
    str--->int"""
    x=str.split(texto,'.')
    y=str.split(texto,'!')
    z=str.split(texto,'?')
    h=str.split(texto,'...')
    return len(x+y+z+h)-4