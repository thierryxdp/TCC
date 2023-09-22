def hashtag(s):
    """ retorna a string com # no inicio, meio e fim."""
    return '#' + s[0:(-1//2 - 1)] + '#' + s[(-1//2):0] + '#'