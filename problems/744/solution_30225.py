def hashtag(s):
    """retorna # no ínicio, meio e final de uma string. str-> str"""
    return '#' + s[0:(len(s)/2)] + '#' + s[(len(s))/2:] + '#'