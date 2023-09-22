def maiores(lista,n):
    """dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista que contenha os valores maiores que n"""
    lista_nova=[i for i in lista if i>n]
    return list.sort(lista_nova)