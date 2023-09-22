def filtraMultiplos(lista, n):
    """
    lista,int->lista
    :param lista: Recebe uma lista de numeros
    :param n: Recebe um número
    :param retun: Retorna a lista com todos os elementos da lista original que
    forem divisiveis por n
    """
    lista = [ ]
    numero = 0
    while numero < len(lista):
        if lista[numero] % n == 0:
            lista = lista.append(lista[numero])
            numero = numero + 1
    return lista