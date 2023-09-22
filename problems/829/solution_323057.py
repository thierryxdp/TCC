def soma_h(N):
    ''' função que calcula a soma de frações que se iniciam em um e vão até termo de escolha do usuário no caso a variável N'''
    H=0
    a=list(range(1,N+1))
    for i in a:
        if i>0:
            H=H+1/i
    return round(H,2)