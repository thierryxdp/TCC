def maiores(lista_numero:list,n:int)->list:

    """ Função  que, dada uma lista de números inteiros e um núumero inteiro n,
        retorna outra lista, que contenha todos os numeros da lista origina
        maiores que n.

    """

    list.append(lista_numero,n)
    list.sort(lista_numero)
    pos=list.index(lista_numero,n)
    nova_lista = lista_numero[(pos+1):]
    return nova_lista