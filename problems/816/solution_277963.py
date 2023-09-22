def maiores(numeros, n):
    """Função que dada uma lista de numeros e um numero inteiro (n), retorna 
    outra lista que contenha todos os numeros maiores que n 
    int , int --> int"""
    ordem = list.sort(numeros)
    retira = list.remove(ordem)
    return retira