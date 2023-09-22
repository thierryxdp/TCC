def repetidos(lista):
    """Função que dada uma lista numérica, retorne a quantidade
    de vezes que um número é igual ao seu posterior,
    list -> int"""
    indice = 0
    iguais = 0
    while indice < len(lista):
        if lista[indice] == lista[iguais + 1]:
    		indice += 1
    return iguais