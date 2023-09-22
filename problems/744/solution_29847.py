def hashtag(s):
    '''A função ao receber uma string ira inserir o caractere (#) no início,no meio e no final dela'''
    ''' str, str -> str'''
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s