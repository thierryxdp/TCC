def maiores(numeros,n):
    '''função que, dada uma lista de números inteiros e um número inteiro n, retorne outra lista,
    que contenha todos os números da lista original maiores que n;list,int -> list '''
    a=numeros
    list.extend(numeros,[n])
    a.sort()
    b=list.index(a,n)
    return a[b+1:]