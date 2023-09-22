def hashtag(s):
    '''recebe uma string e ela é modificada pelo símbolo
    # no início, meio e fim
    str -> str'''
    
    return '#' + (s [:float(len(s)/2)]) + '#' + (s[float(len(s)/2):]) + '#'