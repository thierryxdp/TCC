def repetidos(lista):
    """funcao que recebe como entrada uma lista de numeros e retorna o numero de vezes que um elemento da lista é repetido"""
    b = 1
    repetcao = 0
    while b < len(lista):
        if lista[b] == lista[b-1]:
            repeticao = repeticao +1
        b = b+1
    return repeticao