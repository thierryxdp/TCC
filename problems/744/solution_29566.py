def hashtag(s):
    '''função que adiciona hashtags no inicio, meio e fim da função; string -> string'''
    s = '#' + s[:len(s)//2] + '#' + s[len(s)//2:] + '#'
    return s