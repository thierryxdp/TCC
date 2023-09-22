def filtraMultiplos (lista_numeros, n) :
    """Funcao que recebe uma lista de numeros e um numero n e retorna uma outra lista contendo todos os elementos da lista original que sejam mutiplos de n"""
    lista_mult = []
    contador = 0
    while contador < len(lista):
        if int(lista_numeros[contador])%n == 0:
            lista_mult = lista_mult + (lista_numeros[contador],)
        contador = contador + 1
    return list(lista_mult)