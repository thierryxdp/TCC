def hashtag(s):
    '''recebe um valor e insere o caractere # no início, meio
    e fim
    str -> str'''
    metade = len(s)//2
    return '#' + s[0:metade] + '#' + s[metade:-1:] + '#'