def maiores(lista_num,n):
    ''' função que dada uma lista lista_num de números inteiros
    e um número inteiro n, retorna outra lista que contenha todos
    os números da lista original maiores que n;
    list,int-->list'''
    list.append(lista_num,n)
    list.sort(lista_num)
    x=list.index(lista_num,n)
    return lista_num[x+1:]