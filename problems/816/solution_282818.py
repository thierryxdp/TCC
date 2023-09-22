def maiores(lista_numeros,n):
    """Função que adiciona o número n na lista_números e retorna uma lista
    contendo todos os números maiores que n em ordem crescente (trabalha apenas
    com números inteiros)
    list,int"""
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    list.reverse(lista_numeros)
    x=list.index(lista_numeros,n)
    lista_numeros=lista_numeros[:x]
    list.reverse(lista_numeros)
    return lista_numeros