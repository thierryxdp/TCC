def filtraMultiplos(lista, n):
    """Função que recebe uma lista contendo números e 
    um número n restorna outra lista contendo somente 
    os números em lista que sejam múltiplos do número n
    list, int -> list"""
    extencao = len(lista)
    nova_lista = []
    contador = 0
    while contador > extencao:
        if lista[contador]%n == 0:
            nova_lista.append(lista[contador])
        contador += 1
    return nova_lista