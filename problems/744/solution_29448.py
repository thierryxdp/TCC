def hashtag(s):
    '''recebendo uma string, a função coloca um caractere no inicio, meio e fim da string
    str->str'''
    return '#' + s[:(len(s)//2)] + '#' + s[(len(s)//2):] +'#'