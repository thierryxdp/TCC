def faltante (lista: list)-> int:
    """Função que recebe como entrada uma lista de tamanho N-1 contendo números inteiros não
    repetidos de 1 a N, e retorna qual número inteiro que pertence ao intervalor [1,N], mas não
    pertence a lista de entrada."""
    tamanho = len(lista) + 1
    listacerta = list(range(tamanho))
    i = 1
    nao_pertence = 0
    while i <= len(lista):
        if listacerta[i] not in lista:
            nao_pertence = listacerta[i]
        else:
            nao_pertence = listacerta[-1] + 1
        i = i + 1
    return nao_pertence