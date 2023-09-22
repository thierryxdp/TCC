def repetidos(lista):
    """Recebe uma lista de numeros e retorna o numero de vezes que um elemento da lista é igual ao anterior; lista->int"""
    posicao = 0
    repeticao = []
    while posicao < len(lista):
        if lista[posicao] == lista[posicao -1]:
            repeticao.append(1)
        posicao = posicao + 1
    return sum(repeticao)