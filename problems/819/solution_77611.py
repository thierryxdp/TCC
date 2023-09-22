def filtramultiplos(lista, n):
    '''Função que recebe uma lista e um número, retornará uma outra lista 
       que contem números da lista de entrada que forem divisíveis 
       por n.
       tipo de entrada: list e int
       tipo de saída: list'''
    lista_final = []
    result = 0
    
    while result < len(lista):
        if lista[result] % n == 0:
            lista_final1 = lista_final + [lista[result]]
        result = result + 1
        return lista_final1