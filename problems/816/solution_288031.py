def maiores (listaNumeros, n):
    """ defina uma lista de numeros interios e um numero inteiro n
    Retorna uma lista contendo todos os numeros da lista original maiores que n em ordem crescente"""
    lista = []
    i=0
    N = ( n == max(listaNumeros) )
    if N is True: 
        return lista
    while (n < listaNumeros[i]):
        lista = lista + listaNumeros[i] 
    i = i + 1
    return lista