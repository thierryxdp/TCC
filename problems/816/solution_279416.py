def insere(lista_numero, n):
    lista_com_n = lista_numero + [n,]
    list.sort(lista_com_n)
    return lista_com_n

def maiores(lista_num, n):
    '''dada uma lista de números inteiros e um outro número inteiro n qualquer,
    retorna uma lista com todos os elementos da lista original maiores que n;
    lista, int --> lista'''
    lista_com_n = insere(lista_num, n)
    posicao_n = list.index(lista_com_n,n)
    return lista_com_n[posicao_n+1:]