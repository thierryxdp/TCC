def maiores(lista,n):
    """Cálculo de uma função que dada uma lista de números e um numero inteiro n
    retorna outra lista que contenha todos os números da lista original maiores que n.
    
    Parameters:
    lista: corresponde a lista de números inteiros
    n: corresponde a um número inteiro 
    
    Returns:
    Retorna uma lista de números maiores que n, dado que:
    list, int -> list
    """
    l1=lista[:]
    list.append(l1,n)
    list.sort(l1)
    p=list.index(l1,n)
    return l1[p+1:]