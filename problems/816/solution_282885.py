def maiores(lista, n):
    """retorna uma com todos os numeros maiores que o numero inteiro inserido
    list,int->list"""
    numeros = [lista for lista in lista if lista > n]
    return numeros