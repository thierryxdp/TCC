def hashtag(s):
    """Retorne o caractere '#' no início, meio e fim de uma string"""
    return "#" + str(s)[0:len(s)//2] + "#" + str(s)[len(s)//2:] + "#"