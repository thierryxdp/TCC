def faltante(lista):
    """ dada uma lista de 1 a n de números inte
    número esta faltando;iros, retornta qual
    list -> int"""
    lista_completa = list(range(1, len(lista)))
    i = 0
    conta = 1
    while (i < len(lista_completa)):
        if lista[i] != lista_completa[i]:
            conta += i
        i += 1
    return conta