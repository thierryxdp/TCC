def posLetra(txt, s, n):
    """str, str, int -> int;
    Função que recebe como entrada uma string, uma letra e um
    número que indica a ocorrência desejada da letra (1 para
    a primeira ocorrência, 2 para a segunda, etc.), e retorna
    a posição da string aquela ocorrência da letra está.
    Caso exista menos ocorrências do que a ocorrência pedida,
    a função retorna -1."""
    o = 0
    for i in txt:
        if txt[i] == s:
            o = o + s
        if o == n:
            return i
    return int(-1)