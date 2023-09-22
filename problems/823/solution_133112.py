def faltante(lista):
    """ dada uma lista de 1 a n de números inte
    número esta faltando;iros, retornta qual
    list -> int"""
    lista_completa = list(range(1, lista[-1] + 2))
    i = 0
    conta = 0
    while (i < len(lista_completa) and conta == 1):
        if lista[i] != lista_completa[i]:
            conta += lista[i]
        i += 1
    return conta