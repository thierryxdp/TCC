def maiores(l, n):
    """função que dado uma lista de números inteiros e um numero inteiro n, retorna outra, 
    que contenha todos os elementos da lista original maiores que n: list->list"""
    if n not in l:
        list.insert(l,0,n)
    list.sort(l)
    
    f = list.index(l,n)
    l2 = l[f+1:]
    
    return l