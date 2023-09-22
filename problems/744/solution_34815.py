def hashtag(s):
    '''str -> str'''
    '''retorna uma string com '#' na primeira posição, no meio e no finao da palavra, palavra dada por s'''
    pre = s[:len(s)//2]
    pos = s[len(s)//2:]
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s