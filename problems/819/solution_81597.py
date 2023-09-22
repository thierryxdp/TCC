def filtra_multiplos(lista,n):
    """Tem como objetivo receber uma lista de números inteiros e um número
inteiro. Retornando uma lista apenas com os números da lista que são divisiveis
pelo número dado.
lista,int > lista"""
    lista_valida = []
    for elem in lista:
        if elem%n==0:
            lista_valida.append(elem)
    return lista_valida