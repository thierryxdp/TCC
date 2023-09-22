def soma_h(n):
    """ calcula e retorna o valor do somatório h
    int-->float"""
    s=(1/n)
    lista=[]
    soma=0
    for var in range(1,n+1):
        soma=var+s
    return round(soma,2)