def hashtag(s):
    '''recebe uma string e retorna o caractere # no início, no meio e no fim da string'''
    return "#" + s[0:(len(s)//2)] + "#" + s[(len(s)//2):] + "#"