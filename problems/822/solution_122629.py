def repetidos (lista):
    """funçao que recebe uma lista de numeros e retorna quantas vezes na sequencia um numero e igual ao anterior;
entrada: list;
saida: int."""

    pos = 1
    vezes = 0

    while pos < len (lista):
        if lista [pos] == lista [pos - 1]:
            vezes = vezes + 1

        pos = pos +1
    return vezes