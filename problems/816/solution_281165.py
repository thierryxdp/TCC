def maiores(lista, n):
    '''dada uma lista(lista) composta por numeros inteiros e um numero inteiro(n), retorna a lista de numeros maiores que (n) contidos na lista original(lista); list,int -> list'''
    if n in lista:
        list.sort(lista)
        N = (list.index(lista,n))
        A = lista[(N+1):]
    elif n not in lista:
        lista = lista + [n]
        list.sort(lista)
        N = (list.index(lista,n))
        A = lista[(N+1):]
    return A