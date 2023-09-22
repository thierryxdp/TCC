def soma_h(N):
    '''funçao que calcula o valor de h com n termos; int->float'''
    i=0
    for elem in range(1,N+1):
        h=1/elem
        i=i+h
    return round(i,2)