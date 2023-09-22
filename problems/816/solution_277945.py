def maiores(lista_numeros, n):
    """Função que dada uma lista de numeros e um numero inteiro (n), retorna 
    outra lista que contenha todos os numeros maiores que n 
    int , int --> int"""
    sub_s1 = lista_numeros[: :1]
    sub_s2 = lista_numeros.replace(sub_s1, n , 1)
    return sub_s2