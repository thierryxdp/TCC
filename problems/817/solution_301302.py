def maiores(x,y):
    w=([i for i in x if i>y])
    return sorted (w)

def acima_da_media(x):
    '''
    '''
    y=sum(x)
    z=len(x)
    w=y/z
    return maiores(x,w)