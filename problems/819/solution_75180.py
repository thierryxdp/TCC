def filtraMultiplos(lista_de_numeros,n):
    """Esta é a função que dada uma lista de números e um número, retorna uma outra lista apenas com os elementos da lista dada que são divisíveis pelo número n; list, int -> list"""
    lista = lista_de_numeros
    lista_oficial = [elem for elem in lista if elem%n==0]
    return lista_oficial