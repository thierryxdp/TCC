def hashtag(s):
    '''retorna uma string com o caractere # no seu inicio, meio e fim
    str->str'''
    return '#'+ s+ '#'[len(s)//2:len(s)] +'#'