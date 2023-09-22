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

def acima_da_media(lista_notas):
    """Dada uma lista com as notas dos alunos, a função retorna uma
    lista ordenada com as notas que ficaram acima da média;
    list -> list"""
    quantidade_de_alunos = len(lista_notas)
    media = sum(lista_notas)/quantidade_de_alunos
    lista1 = maiores(lista_notas,media)
    return lista1