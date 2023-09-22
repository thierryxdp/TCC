def hashtag(s):
    '''dada uma str s, retorna retorna a mesma str com o caractere #
    no início, no meio e no final; str->str'''
    m=int(len(s)/2)
    return '#'+s[0:m]+'#'+s[m:len(s)]+'#'