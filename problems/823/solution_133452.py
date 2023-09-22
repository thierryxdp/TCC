def faltante(lista):
    """Função que dada uma lista de inteiros numerados de 1 a n, retorna qual número inteiro está faltando
lista -> int"""

    lista_ordenada = sorted(lista)

    if lista_ordenada[0] != 1:
        return 1

    proximo = 0
    valor = 0
    
    while proximo <len(lista_ordenada):
        if lista_ordenada[proximo] + 1 not in lista_ordenada:
            valor = lista_ordenada[proximo] + 1
        proximo = proximo + 1
    return valor