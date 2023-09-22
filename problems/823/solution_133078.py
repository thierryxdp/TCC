def faltante(lista):
    """ dada uma lista de 1 a n de números inteiros, retornta qual
    número esta faltando;
    list -> int"""
    i = 0
    conta = 1
    lista_completa = list(range(1, len(lista))
    while (i < len(lista_completa) and conta) = 0:
        if lista[i] != lista_completa[i]:
            conta += i
        i += 1
        return conta