def repetidos (lista):
    """funcao que dada uma lista de números, retorne o número
    de vezes que um elemento da lista é igual ao anterior"""
    """list -> int"""
    i = 0
    repetidos =  0

    while i < len(lista) - 1:
        if lista[i] == lista[i+1]:
            repetidos += 1
        i += 1
    return repetidos