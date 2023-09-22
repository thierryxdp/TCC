def filtraMultiplos(lista_de_numero, n):
    '''Função que filtra os múltiplos de um número, retorna outra lista contendo
       todos os elementos da lista originalque eorem divisíveis por n.
       lista,int ---> lista'''
    lista = []
    num = 0
    while num < len(lista):
        if lista [num] in n == 0:
            lista = lista + [lista[num]]
            num = num + 1
    return lista