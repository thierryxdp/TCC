def hashtag(s):
    '''dada uma str, retorna a str com a # no ínicio,meio e fim;str->str'''
    s=+str('#')+s+s[-1]+str('#')
    return s