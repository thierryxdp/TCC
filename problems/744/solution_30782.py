def hashtag(s):
    ''' Essa funçao coloca o simbolo de hashtag no começo, meio e fim de uma string.
    str -> str'''
    i = len(s)
    if i % 2 == 0:
        return '#' + s [0: i] + '#" + s[i +1 : ]
    else:
        return '#' + s[0: i + 1] + '#' + s[ i+2: ]