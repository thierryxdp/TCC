def maiores(lista,n):
    """ dada uma lista de números inteiros 
    a função retorna uma nova com os números 
    da lista original maiores que n em ordem.
    assinatura: list --> list
    testes:
    maiores([2,4,57,21],1) ==[2,4,21,57]
    maiores([2,4,57,21],10) ==[21,57]
    maiores([2,4,57,21],1) ==[2,4,21,57]
    """
    list.append(lista,n)
    list.sort(lista)
    return lista[list.index(lista,n) + 1:]