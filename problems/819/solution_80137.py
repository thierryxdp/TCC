def filtraMultiplos(lista_de_numeros, n):
    """Recebe uma lista de números e um numero e retorna os múltiplos
    do número contidos na lista;
    list, int -> list"""
    lista_multiplos = []
    i = 0
    while i < len(lista_de_numeros):
        if lista_de_numeros[i]%n == 0:
            lista_multiplos.append(lista_de_numeros[i])
        i += 1
    return lista_multiplos