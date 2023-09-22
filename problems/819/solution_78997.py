def filtraMultiplos(lista, numero):
    """Função que, dada uma lista de números e um número, retorna outra lista contendo
    todos os números divisíveis pelo número."""

    return list(filter(lambda num:num%n == 0, lista))