def hashtag(s):
    ''' Essa funçao coloca o simbolo de hashtag no começo, meio e fim de uma string.
    str -> str'''
    if len(s) % 2 == 0:
        return '#' + s [len(s)%2-1 : len(s)%2+ 4] + '#' + s[ len(s)%2+ 5: ] + '#' 
    else:
        return '#' + s[0: len(s)%2 ] + '#' + s[ len(s)%2: ] + '#'