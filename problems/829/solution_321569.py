def soma_h(n):
    """ calcula e retorna o valor do somatório h
    int-->float"""
    s=((1)+(1/n+1))
    soma=0
    for var in range(n+1):
        soma=soma+s
    return round(soma,2)