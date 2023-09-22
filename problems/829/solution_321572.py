def soma_h(n):
    """ calcula e retorna o valor do somatório h
    int-->float"""
    soma=0
    for var in range(1,n+1):
        s=(1/n)
        soma=soma+s
    return round(soma,2)