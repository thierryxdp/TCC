def hashtag(s):
    """funcao que insere hashtag no começo, meio e fim da string
   str -> str"""
    return '#' + s[:len(s)//2:] + '#' + s[len(s)//2:] + '#'