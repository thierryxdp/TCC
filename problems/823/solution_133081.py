def faltante(lista):
    """ dada uma lista de 1 a n de números inteiros, retornta qual
    número esta faltando;
    list -> int"""
    i = 0
    lista_completa = list(range(1, len(lista))
    conta = 1
    while (i < len(lista_completa) and conta) = 0:
        if lista[i] != lista_completa[i]:
            conta += i
        i += 1
    return conta