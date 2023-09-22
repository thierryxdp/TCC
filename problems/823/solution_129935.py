def faltante(lista):
    """Esta é a função que dada uma lista com N-1 inteiros numerados de 1 a N(não repetidos), retorne o número inteiro deste intervalo que está faltando; list -> int"""
    
    lista = sorted(lista)
    lista1 = list(range(1,lista[-1])) + [lista[-1]]
    soma_lista = sum(lista)
    soma_lista1 = sum(lista1)
    x = soma_lista1 - soma_lista

    if x != 0:
        return x

    else:
        return int(lista[-1] + 1)