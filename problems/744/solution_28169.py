def hashtag(s):
    '''Função que retorna hashtags no início, meio e fim de uma string
    Parâmetros: str -> str'''
    metade = len(s)//2
    return "#" + s[0:metade] + "#" + s[metade:] + "#"