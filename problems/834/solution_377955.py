def media_matriz(m):
    """Retorna a média de todos os números da matriz. 
    list -> int"""
    somafinal=0
    for i in range(len(m)):
        soma = sum(m[i])
        somafinal = somafinal+soma
    return round(somafinal,2)