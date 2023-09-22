def hashtag(s):
    '''Função que, dada uma string s, retorna essa mesma string com # no início, no meio e no final.
    str-> str'''
    return '#' + s[0:(len(s)//2)] + '#' + s[(len(s)//2):] + '#'