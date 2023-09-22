def repetidos(lista_num):
    """"Esta função recebe uma lista e retorna a quantidade de vezes em que um elemento da lista é igual ao anterior.
    list -> int"""
    return (len(lista_num)-len(set(lista_num)))