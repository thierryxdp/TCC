def hashtag(s):
    """funcao que insere hashtag no inicio, meio e fim de s
    entrada: str
    saida: str"""
    return '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'