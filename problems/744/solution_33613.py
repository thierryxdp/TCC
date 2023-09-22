def hashtag(s):
    '''Função que recebe uma string s e insere
    o caractere # no início, meio e fim da string
    str->str'''
    s[0] = inicio
    s[-1] = fim
    return s.join('#',inicio)