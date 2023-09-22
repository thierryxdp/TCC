def posLetra(txt, s, n):
    """str, str, int -> int;
    Função que recebe como entrada uma string, uma letra e um
    número que indica a ocorrência desejada da letra (1 para
    a primeira ocorrência, 2 para a segunda, etc.), e retorna
    a posição da string aquela ocorrência da letra está.
    Caso exista menos ocorrências do que a ocorrência pedida,
    a função retorna -1."""
    if n == 1:
        return str.find(txt, s)
    return -1