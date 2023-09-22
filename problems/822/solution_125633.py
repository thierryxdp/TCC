def repetidos(lista):
    """funcao que dada de entrada uma lista de numeros,
    retorna o numero de vezes que um elemento da lista  ́e
    igual ao elemento anterior;
    list -> int"""
    
    L = []
    numero = 1
    while numero < len(lista):
        if lista[(numero)] == lista[(numero-1)]:
                 L = L + [numero]
        numero = numero + 1
    return len(L)