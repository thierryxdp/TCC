def faltante(lista):
    """função que dada uma lista com N-1, descobre qual o 
    número inteiro deste intervalo está em falta
    lista -> int"""
    total = list(range(1,len(lista)+2))
    s1 = sum(total)
    s2 = sum(lista)
    return s1 - s2