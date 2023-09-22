def maiores(lista,n):
    '''Função que dada uma lista de números inteiros e um número inteiro n, retorna outra
     lista, que contenha todos os números da lista original maiores que n ordenados em ordem crescente.
     List[int]->list[int]'''

    L=lista
    list.append(L,n)
    list.sort(L)
    indece=list.index(L,n)
    novo_indece=indece+1
    L=L[novo_indece:]
    return L