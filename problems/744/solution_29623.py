def hashtag(s):
    '''recebe uma string e ela pe modificada pelo símbolo
    # no início, meio e fim
    str -> str'''
    
    return '#' + s [:len()/2] + '#' + s[len()/2 + 1:] + '#'