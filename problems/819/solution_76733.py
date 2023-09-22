def filtraMultiplos (lista_numeros, numero):
    """Recebe uma lista de números, e um número qualquer.
    Retorna uma nova lista de números, contendo apenas os
    múltiplos do número informado no segundo parâmetro.
    list, int -> list"""
    indice = 0
    nova_lista = []
    while indice < len(lista_numeros):
        if lista_numeros[indice] % numero == 0:
            list.append(nova_lista, lista_numeros[indice])
        indice += 1
    return nova_lista