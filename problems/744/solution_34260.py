def hashtag(s):
    '''retorna uma string com caractere # no seu inicío, meio e fim
    str->str'''
    return '#'+ s[len(s)-3:len(s)] +'#'