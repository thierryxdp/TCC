def repetidos(lista):
    """Dada uma lista de numeros, retorna quantas vezes um numero dessa
    lista é igual ao seu antecessor"""
    i = 1
    n = 0
    while i<len(lista):
        if lista[i] == lista[i-1]:
            n = n + 1
        i = i + 1
    return n