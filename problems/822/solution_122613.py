def repetidos(lista):
    """Dada uma lista de numeros, retorna quantas vezes um numero dessa
    lista é igual ao seu antecessor"""
    i = 0
    n = 0
    while i<len(lista):
        if lista[i+1] == lista[i]:
            n = n +1
        i = i + 1
    return n