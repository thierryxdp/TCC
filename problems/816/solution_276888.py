def maiores(lista):
    '''Recebe uma lista de números e um número n, e retorna outra lista com todos os números maiores que n.
list, int -> list'''
    lista_1 = lista[0]
    n = lista[1]
    larger_elements = [element for element in lista_1 if element > n]
    print(larger_elements)