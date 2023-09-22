def faltante(lista):
    """Função que dada uma lista com N-1 inteiros numerados de 1 a N,
retorna o número do intervalo que está faltando; list -> int"""
    lista.sort()
    n = 1
    indice = 0
    while n in lista:
        n+=1
    return n