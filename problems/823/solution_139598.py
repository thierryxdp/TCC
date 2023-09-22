def faltante(lista_pecas):
    """função que dada uma lista com N-1 inteiros numerados de 1 a N, descobre qual número inteiro está  faltando
    lista -> int"""
    valores = sorted(lista_pecas)
    for i in range(len(valores)):
        if i + 1 != valores[i]:
            return i + 1
    return len(valores) + 1