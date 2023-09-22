def peca_perdida(lis):
    '''
    '''
    i=0
    n=len(lis)+1
    soma=0
    while i<len(lis):
        soma= soma+ lis[i]
        i=i+1
        return (n*(n+1)/2)-soma