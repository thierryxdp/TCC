def insere(lista_numero,n):
    """Dada uma lista ordenada de forma crescente de números inteiros e um número inteiro 'n',
    a função retorna uma outra lista com 'n' incluido em uma posição que mantenha a lista na ordenada;
    list, int -> list"""
    list.insert(lista_numero,0,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista_num,n):
    """Dada uma lista de números inteiros e um número inteiro 'n', a função retorna outra
    lista que contém todos os números da lista original que são maiores do que 'n';
    list, int -> list"""
    if n in lista_num:
        list.sort(lista_num)
        indice = list.index(lista_num,n)
        del lista_num[0:indice+1]
        return lista_num
    else:
        lista1 = insere(lista_num,n)
        indice = list.index(lista1,n)
        del lista1[0:indice+1]
        return lista1