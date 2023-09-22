def maiores(lista,n):
    """dada uma lista de números inteiros e um numero inteiro n
    retorna outra lista que contenha todos os números da lista original
    maiores que n em ordem crescente
    list,int->list"""
    a=([i for i in lista if i > n])
    return sorted(a)