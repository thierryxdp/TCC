def maiores_que(lista,n):
    """Retorna os valores maiores que n de uma lista de numeros;lista,int=>lista"""
    lista=list( filter( lambda e: e >= n , lista ) )
    return lista