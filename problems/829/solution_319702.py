def soma_h(N):
    '''Retorna a soma de 1 mais as divisões de 1 por todos os valores até N'''
    soma=1
    for i in range(N+1):
        if i!=0:
        soma=soma+1/i
    return round(soma,2)