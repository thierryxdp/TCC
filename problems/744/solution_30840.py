def hashtag(s):
    """ retorna a string com # no inicio, meio e fim."""
    return '#' + s[:abs(-1//2)] + '#' + s[abs(-1//2):] + '#'