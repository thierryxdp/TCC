def maiores(lista,n):
    '''funcao que dada uma lista de numeros inteiros e um numero 
    inteiro, retorna outra lista que contem todos os numeros da lista 
    original maiores que n, ordenados em ordem crescente.
    list,int->list'''
    a=([i for i in lista if i > n])
    list.sort(a)
    return a