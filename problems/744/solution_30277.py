def hashtag(s):
    """retorna a mesma string com # no ínicio, meio e fim. str-> str"""
    return '#' + s[0:(len(s)//2)] + '#' + s[(len(s)//2):] + '#'