def hashtag(s):
    '''Escreva uma funcão que receba ''#'' no inicio, meio e fim'''
    s = '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'
    return s