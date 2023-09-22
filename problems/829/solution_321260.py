def H(N):
    '''Função que gera a série da soma H. int->list.'''
    s=[]
    for n in range(1,N):
        k=1/n
        list.append(s,k)
    return s
def soma_h(N):
    '''Função que gera a Soma H. int->float.'''
    s=H(N)
    soma=sum(s)
    return round(soma,2)