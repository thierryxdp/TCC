len
def hashtag(s):
    '''Insere um # no início, meio e fim de uma string'''
    x=len(s)//2
    return str('#')+hashtag[:x]+str('#')+hastag[x:]