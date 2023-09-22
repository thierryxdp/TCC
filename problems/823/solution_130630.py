def faltante(lista):
    """Recebe uma lista com n números representativos de cada peça de um quebra-
    cabeça, e retorna o número inteiro que pertença ao intervalo dessa lista mas
    que não tenha sido informado
    list -> int"""
    lista_completa = list(range(len(lista)))
    i = 0
    while (i < len(lista)):
        if lista[i] not in lista_completa:
            return lista[i]
        i += 1