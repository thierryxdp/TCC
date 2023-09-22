def hashtag(s):
    '''recebe uma string e ela é modificada pelo símbolo
    # no início, meio e fim
    str -> str'''
    
    return '#' + (s [:(len(s)//2)]) + '#' + (s[(len(s)//2):]) + '#'