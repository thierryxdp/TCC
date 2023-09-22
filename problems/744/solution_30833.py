def hashtag(s):
    """ retorna a string com # no inicio, meio e fim."""
    return '#' + s[0:abs(-1//2 - 1)] + '#' + s[abs(-1//2):0] + '#'