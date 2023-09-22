def maiores(lista_numero,n):
    """
    Função que dados, respectivamente, uma lista ordenada(crescente)
    de numeros inteiros, e um número inteiro, retorna uma lista somente com
    os numeros maiores que n
    list , int ---> list
    """
    l1=lista_numero+[n]
    list.sort(l1)
    indice=(list.index(l1,n))+1
    return l1[indice:]