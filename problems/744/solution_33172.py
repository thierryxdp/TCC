def hashtag(s):
    '''dada uma str, retorna a str com a # no ínicio,meio e fim;str->str'''
    s=s+str('#')+s[0]+str('#')+s[:len(s)//2]+s[-1]+str('#')
    return s