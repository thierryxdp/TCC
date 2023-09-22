def maiores(lista_numeros,n):
    '''Função que retorna outra lista, que contenha todos os
números da lista de entrada maiores do que n, em ordem
crescente;
    lista,int -> lista'''
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    p=list.index(lista_numeros,0,-1)
    del lista_numeros[0:p+1]
    return lista_numeros