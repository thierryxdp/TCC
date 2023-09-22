def maiores(numeros, n):
    """Função que dada uma lista de numeros e um numero inteiro (n), retorna 
    outra lista que contenha todos os numeros maiores que n 
    int , int --> int"""
    lista1 = list.sort(numeros)
    return list.remove(numeros, n )