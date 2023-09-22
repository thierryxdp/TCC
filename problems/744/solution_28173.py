#hashtag
def hashtag(imf):
    """funcao que retorna # no inicio, meio e fim de uma string,
       str --> str"""
    x = (len(imf)//2)
    return '#'+ imf[0:x]+'#'+imf[x:]+'#'