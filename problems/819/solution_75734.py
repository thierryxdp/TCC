def filtraMultiplos (lista, n):
    '''Dada uma lista com números e um número, a função retorna uma lista
       com quais números da lista original são divisíveis pelo número
       escolhido.
       list, int -> list
       Parametros:
       lista: lista contendo números
       n: numero que sera o divisor'''
    lista2 = []
    i = 0
    while i < len(lista):
        if lista[i] % n == 0:
            lista2.append(lista[i])
        i += 1
    return lista2