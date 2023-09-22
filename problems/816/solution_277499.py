def maiores(a,n):
    """funcao que dado uma lista com numeros inteiros e um numero inteiro n ela retorna outra lista com todos os numeros inteiros maiores que n, que estao na lista original
    lista,int->lista"""
    list.append(a,n)
    list.sort(a)
    x=list.index(a,n)
    b=a[x:]
    return list.remove(b,n)