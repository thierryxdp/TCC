def repetidos(lista_num):
    """Recebe uma lista de números e retorna o número de vezes que o número em
    uma posição é igual ao seu antecessor

    list -> int"""
    i = 0
    k = 0
    while(i < len(lista_num)):
        if (lista_num[i] == lista_num[i - 1]):
            k += 1
        i += 1
    return k