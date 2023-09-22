def faltante(lista):
    """Dada uma lista de N-1 inteiros numerados de 1 a N retorna qual está faltando;
    lista -> int"""
    n=1
    while n<(len(lista)+2):
        if n not in lista:
            return n
        n+=1