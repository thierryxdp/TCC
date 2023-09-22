def hashtag(s):
    """ retorna a string com # no inicio, meio e fim."""
    A = len(s)//2 - 1
    return '#' + s[:A] + '#' + s[A:] + '#'