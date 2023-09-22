def media_matriz (matriz):
    """funçao que recebe uma matriz e retorna a media dos numeros contidos nela;
    entrada: list;
    saida: float."""
    soma = 0
    vezes = 0
    for i in matriz:
        for j in i:
            soma += j
            vezes += 1
    media = soma / vezes
    return round (media,2)