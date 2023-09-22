def repetidos(lista):
    """Dada a lista de entrada, retorna o numero de vezes que um elemento é igual ao seu antecessor;
    list -> int"""
    
    i = 1
    contador = 0
    
    while i < len(lista):
        if lista[i] == lista[i-1]:
            contador += 1
        i += 1
    return contador