def maiores(lista,n):
    """Retorna os valores maiores que n de uma lista de numeros;lista,int=>lista"""
    lista=list( filter( lambda e: e >= n , lista ) )
    return lista
def acima_da_media(lista): 
    b=len(lista)
    c=sum(lista)
    n=c/b
    a=maiores(lista,n)
    a=a.sort()
    return a