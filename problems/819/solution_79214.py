def filtraMultiplos(lista_numeros, n):
    '''Filtra de uma lista os mútiplos de um número n;
       list, int -> list'''
    contador = 0
    lista_multiplos = []
    while contador < len(lista_numeros):
        if lista_numeros[contador]%n == 0:
            lista_multiplos.append(lista_numeros[contador])
        contador = contador + 1
    return lista_multiplos