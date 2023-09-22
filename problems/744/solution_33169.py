def hashtag(s):
    '''dada uma str, retorna a str com a # no ínicio,meio e fim;str->str'''
    s=str('#')+s[0]+s[:len(s)//2]+str('#')
    return s