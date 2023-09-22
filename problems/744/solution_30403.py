len
def hashtag(s):
    '''Insere um # no início, meio e fim de uma string'''
    return str('#')+hashtag[:len(s)//2]+str('#')+hastag[len(s)//2:]