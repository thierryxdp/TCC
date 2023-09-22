def qtd_divisores(N):
    '''
    Função recebe um número e conta a quantidade de divisores
    Retorna a quantidade de divisores se N>1 e "0" se N<=0
    '''
    if N<=0:
        return 0
    n = 1
    num=[]
    while(n<N):
        if(N%n==0):
            num.append(n)
        else:
            pass
        n += 1
    num.append(N)
    return len(num)