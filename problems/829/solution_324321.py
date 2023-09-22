def soma_h(n):
    '''Essa função calcula o valor de H com n termos,
    int->int'''
    soma=0
    for x in range(1,n+1):
        soma+=1/x
    return soma