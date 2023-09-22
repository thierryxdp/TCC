def soma_h(n):
    """ calcula e retorna o valor do somatório h
    int-->float"""
    lista=[]
    for var in range(1,n+1):
        s=(1/var)
        list.insert(lista,0,s)
    soma=sum(lista)
    return round(soma,2)