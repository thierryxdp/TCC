def hashtag(s):
    """A função adiciona um caractere "#" no começo, meio e fim de uma string imputada.
    assinatura: str --> str
    """
    return '#' + s[0:len(s)//2] + '#' + s[len(s)//2:] + '#'