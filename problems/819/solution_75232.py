def filtraMultiplos(lista_de_numeros,n):
    """Esta é a função que dada uma lista de números e um número, retorna uma outra lista apenas com os elementos da lista dada que são divisíveis pelo número n; list, int -> list"""
    lista = []
    proximo = 0
    while proximo < len(lista_de_numeros):
        if lista_de_numeros[proximo]%n == 0:
            lista = lista + [lista_de_numeros[proximo]]
        proximo = proximo + 1
    return lista