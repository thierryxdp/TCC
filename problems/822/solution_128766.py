def repetidos(lista):
    """funcao que recebe como entrada uma lista de numeros e retorna o numero de vezes que um
    elemento da lista e igual ao elemento anterior;
    list -> int"""
    i = 0
    qtd = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            qtd = qtd + 1
        i = i + 1
    return qtd