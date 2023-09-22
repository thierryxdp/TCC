def maiores(lista,n):
    """funcao que dada uma lista de numeros e um num inteiro n , retorna outra 
    lista q contem todos os numeros maiores que o numero inteiro inserido"""
    numeros = [lista for lista in lista if lista > n]
    return numeros