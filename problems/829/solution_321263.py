def H(N):
    '''Função que calcula a série dos termos da Soma H. int->list.'''
    s=[]
    for n in range(1,N+1):
        k=1/n
        list.append(s,k)
    return s
def soma_h(N):
    '''Função que calcula a Soma H. int->float.'''
    s=H(N)
    soma=sum(s)
    return round(soma,2)