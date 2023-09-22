def maiores(L,n):
    '''Função que dada uma lista de números inteiros e um número inteiro n, retorna outra
    lista, que só contém os números da lista L maiores que n. Entrada: list, int.
    Saída:list'''
    list.append(L,n)
    list.sort(L)
    indice=list.index(L,n)
    return L[(indice+1):]