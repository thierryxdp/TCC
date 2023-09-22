def hashtag(s):
    """Função que contatena o caracter # no começo, meio e fim da string dada na entrada."""
    return '#' + s[0:int(len(s)/2)] + '#' + s[int(len(s)/2):len(s)] + '#'