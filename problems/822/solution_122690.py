def repetidos (lista):
    """funçao que recebe uma lista com numeros e retorna o numero de vezes que na sequencia um numero e igual ao elemento anterior;
entrada: list;
saida: int."""
    pos = 1
    i = 0
    while pos < len (lista):
        if lista [pos] == lista [pos - 1]:
           i +=  1
        pos += 1
    return i