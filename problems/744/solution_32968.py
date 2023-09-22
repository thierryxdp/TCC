def hashtag(s):
    ''' funcao chamada hashtag que recebe uma string e insere o caractere # no inicio, no meio e no final dela.
    str->str'''
    media = len(s)//2
    return "#" + s[0:media] + "#" + s[media:]+ "#"