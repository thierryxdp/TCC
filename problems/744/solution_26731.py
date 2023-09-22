def hashtag(s):
    '''função retorna string inserida com o caractere "#" em seu começo, meio e fim
    str -> str'''
    x = len(s)//2
    return '#' + s[:x] + '#' + s[x:] + '#'