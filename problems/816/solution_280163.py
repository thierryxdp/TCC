def maiores(lista, n):
    '''Função que dada uma lista de inteiros e um número (n), 
    retorna outra lista com todos os números maiores que n.
    entrada da função: list e int
    saída da função: list'''
    list.sort()
    x = list.index(n)
    lista2 = lista [x + 1 :]
    y = lista2.count(n)
    
    return lista2[y:]