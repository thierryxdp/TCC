def hashtag(s):
    """ retorna a string com # no inicio, meio e fim."""
    a = s[-1] // 2
    return '#' + s[0:a] + '#' + s[2:-1] + '#'