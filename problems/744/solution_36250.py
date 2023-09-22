def hashtag(s):
    'Função que recebe uma string e insere um caractere # no meio e final'
    #str->str#
    return '#' + s[:len(s)//2:]+ '#' + s[len(s)//2:] + '#'