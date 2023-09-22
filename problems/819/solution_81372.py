def filtraMultiplos(lista, numero):
    """Dada uma lista e um número, a função irá checar quais elementos da lista
    são divisíveis pelo número, e retornará uma nova lista com os números divisíveis.
    Tipo da varável lista: list
    Tipo da variável número: int
    Tipo de saída: list"""
    contador = 0
    nova_lista = []
    while contador < len(lista):
        if lista[contador]%numero == 0:
            list.append(nova_lista, lista[contador])
		contador = contador + 1
    return nova_lista