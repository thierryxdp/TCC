def maiores(lista,n):
    '''Funçao que, dada uma lista de numeros inteiros e 
    um numero inteiro (n), retorna outra lista que contem todos
    os numeros da lista original maiores que o numero fornecido,
    organizados em ordem crescente.
    list,int->list'''
    a=([i for i in lista if i > n])
    return sorted(a)