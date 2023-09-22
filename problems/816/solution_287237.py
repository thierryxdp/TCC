def maiores(lista, n):
    """Recebe uma lista de valores inteiros e um valor inteiro n, retornando uma nova lista
    com todos os valores maiores que n
    assinatura: list, int --> list
    testes:
    maiores([3, 4, 5], 2)==[3, 4, 5]
    maiores([2, 5, 6], 3)==[5, 6]
    """
    n=n   
    lista.append(n)
    list.sort(lista)  
    lista2=filter(lista > n , lista)
    return lista2