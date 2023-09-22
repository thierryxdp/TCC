def posLetra(texto,letra,ocorrencia):
    """Função que recebe uma string, uma letra e um número. O número indica a
        ocorrência desejada da letra (1 para primeira ocorrência,
        2 para segunda, etc). A função deve retornar em que posição da string
        aquela ocorrência da letra está. Caso exista menos ocorrências
        da letra do que a ocorrência pedida, a função deveretornar -1."""
    i = 0
    n = 0
    while i<len(texto) and n<ocorrencia:
        if texto[i] == letra:
            n = n +1
        i = i + 1
    if n < ocorrencia:
        return -1
    else:
        return i-1