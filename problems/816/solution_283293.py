# A função recebe uma lista de números inteiros e um número inteiro n e retorna outra lista que
# contenha todos os números da lista original maiores que n, ordenados em ordem crescente
# list,int->list

def maiores(lista_inteiros,n):
    list.append(lista_inteiros,n)
    list.sort(lista_inteiros)
    i=list.index(lista_inteiros,n)
    lista_inteiros=lista_inteiros[-1:i:-1]
    list.reverse(lista_inteiros)
    return lista_inteiros