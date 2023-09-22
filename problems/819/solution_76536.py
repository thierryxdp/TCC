def filtraMultiplos(L,n):
    """uma função chamada filtraMultiplos para filtrar os múltiplos de um número n. Sua função deve receber como entrada uma lista de números e um número, e retornar outra lista
    contendo todos os elementos da lista original que forem divisíveis por n."""
    i=0
    L2=[]
    while(len(L)>i):
        if L[i] % n == 0:
            L2.append(L[i])
        i=i+1
    return L2