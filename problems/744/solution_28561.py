def hashtag(s):
    """função que insere "#" no início, meio e fim da string de entrada s
    entrada: str
    saída: str"""
    metade = len(s)//2
    
    return '#' + s[0:metade] + '#' + s[metade:] + '#'