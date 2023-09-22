def soma_h(n):
    """calcula a soma de 1+ 1/2+ 1/3... 1/n, dado n como numero de entrada"""
    a= list(range(1,n+1))
    indice=0
    soma=0
    lista=[]
    for indice in a:
        list.append(lista,(1/a[indice]))
    return round(sum(lista),2)