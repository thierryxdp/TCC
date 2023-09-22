def maiores(lista,n):
    """função que dada uma lista e um número, retorna uma lista de números maiores que o que foi dado
 parâmetro de entrada:list,str
 parâmetro de saída list"""
    list.append(lista,n)
    list.sort(lista)
    a = list.index(lista,n)
    nova_lista = lista[-1:a:-1]
    list.reverse(nova_lista)
    return nova_lista