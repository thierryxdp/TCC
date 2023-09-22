def repetidos(lista):
    """
    Função que dada uma lista de números, retorna o número de vezes que um elemento dxa lista é igual ao anterior
    list -> int
    """
    i = 1
    prox = 0
    
    while i< len(lista):
        if lista[i] == lista[i-1]:
            prox += 1
        i += 1
    return prox