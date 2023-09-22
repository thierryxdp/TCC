def maiores(lista_numeros, n):
    """Função que dada uma lista de numeros e um numero inteiro (n), retorna 
    outra lista que contenha todos os numeros maiores que n 
    int , int --> int"""
    lista1 = list.sort(lista_numeros)
    maior = list.remove(lista1,n)
    return maior