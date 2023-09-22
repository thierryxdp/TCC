def soma_h(N):
    '''função acha o valor de H, baseado no número N dado, que delimita o total de somas feitas.int->float'''
    soma=0
    for x in range(1,N+1):
        soma= soma+1/x
    return round(soma,2)