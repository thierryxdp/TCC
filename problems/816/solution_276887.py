def maiores(lista,n):
    '''Recebe uma lista de números e um número n, e retorna outra lista com todos os números maiores que n.
list, int -> list'''
    larger_elements = [element for element in lista if element > n]
    print(larger_elements)