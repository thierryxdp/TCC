def filtraMultiplos(list,n):
    """
    Esta função filtra os múltiplos de um número 'n'
    em uma lista de números chamada 'lista', ela retorna
    uma nova lista ('multi') contendo todos os elementos da lista
    original que forem divisíveis por 'n'
    Parametro de entrada: list, int
    Valor de retorno: list
    """
    i=0
    multi=[]
    while i<len(lista):
        m=lista[i]%n
        if m==0:
            list.append(multi,lista[i])
        i=i+1
    return multi