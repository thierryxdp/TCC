def maiores (lista,n):
    """ A função maiores, dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contem todos os números da lista original maiores que n.
        
        Parameters:
            lista = lista de números inteiros
            n = numero o qual será utilizado para definir quais números serão retornados

        Testes:
            maiores([1,2,4,5],3) = [4,5]
            maiores([1,2,3,4,5],3) = [4,5]

        Returns:
            lista com todos os números da lista original maiores que n
            list, int --> list
    """
    if n in lista:
        vezes = list.count(lista,n)
        list.append(lista,n)
        list.sort(lista)
        local = list.index(lista,n)
        resultado = lista[local+vezes+1:]
    else:
        list.append(lista)
        list.sort(lista)
        local = list.index(lista,n)
        resultado = lista[local+1:]
    return resultado