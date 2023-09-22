def filtraMultiplos (lista,n):
    """funcao que dada uma lista e um numero, retorna uma nova lista com os numeros divisiveis pelo numeros dado
    list -> list"""
    mult = []
    proximo = 0
    
    while proximo <len(lista):
    
    if lista[proximo]%n == 0:
        mult = mult + (lista[proximo],)
    proximo = proximo + 1
    return mult