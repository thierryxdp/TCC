def soma_h(numero):
    '''função que calcula e retorna o valor de H
    int->float'''
    H=[]
    for i in range(1,numero+1):
        if i==0:
            H.append(i)
        else:
            H.append(1/i)
    return round(sum(H),2)