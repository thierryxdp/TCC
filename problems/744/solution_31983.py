def hashtag(s):
    '''Função que, dada uma string insere o caractere # no início,
    no meio e no final dela.
    str->str'''
    media = len(s) //2
    s="#"+s[0:media]+"#"+s[media:]+"#"
    return s