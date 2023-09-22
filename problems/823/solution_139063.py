def faltante(lista):
    """Função que dada uma lista com N-1 inteiros numerados de 1 a N,
retorna o número do intervalo que está faltando; list -> int"""
    x = 1
    while x in lista:
        x+=1
    return x