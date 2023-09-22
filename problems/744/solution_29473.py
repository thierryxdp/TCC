def hashtag(s):
    '''recebe um valor e insere o caractere # no início, meio
    e fim
    str -> str'''
    div = s//2
    return '#' + s[0:s//2] + '#'