def hashtag(s):
    '''insere o # no inicio meio e fim da string.
    str -> str'''
    return '#'+ s[: len(s)//2] + '#' + s[len(s)//2 :] + '#'