def hashtag(s):
    """Função que retorna uma hashtag no inicio, feio e fim da string dada"""
    return '#' + s[:len(s)//2:] + '#' + s[len(s)//2] + '#'