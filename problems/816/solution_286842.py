def maiores (l_num,n):
    '''função em que dada uma lista de números inteiros  e um número inteiro (n)
    retorna outra lista, que contenha todos os números da lista original
    maiores que n ordenados em ordem crescente;
    list, int -> list'''
    list.append(l_num,n)
    list.sort(l_num)
    l1=list.index(l_num,n)
    return l_num[l1+1:]