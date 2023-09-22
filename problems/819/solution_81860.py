def filtraMultiplos(lista,n):
    """ a partir de uma lista de numeros e um numero 
    qualquer n, retorna uma outra lista  contendo todos
    os itens da lista de entrada que forem divisiveis
    pelo valor n
    list, int -> list"""
    lista_multiplos = []
    indice = 0
    while indice < len(lista):
        if lista[indice] % n == 0:
            lista_multiplos += lista[indice]
        indice += 1
    return lista