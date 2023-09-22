def soma_h(n):
    """calcula a soma de 1+ 1/2+ 1/3... 1/n, dado n como numero de entrada"""
    a= range(1,n+1)
    indice=0
    soma=0
    for indice in a:
        soma=soma+(1/a[indice])
    indice=indice+1
    return round(soma,2)