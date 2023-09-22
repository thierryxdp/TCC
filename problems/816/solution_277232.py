def maiores(listaint,n):
    '''função que dada uma lista de números inteiros(listaint) e um número inteiro(n), retorna outra lista que contenha todos os números da lista original maiores que o número inteiro(n).
       parâmetros de entrada:list, int
       valor de retorno:list'''
    lista1=listaint+[n]
    list.sort(lista1)
    procura=list.index(lista,n)
    contagem=list.count(lista,n)
    return lista1[procura+contagem:]