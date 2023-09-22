def repetidos(lista):
    """funcao que retorna o numero de vezes que um elemento de uma lista é igual ao anterior;
    list -> int"""
    

    i = 1
    f = 0

    while i<len(lista):
        if lista[i] == lista[i-1]:

            f = f+1

        i = i+1

    return f