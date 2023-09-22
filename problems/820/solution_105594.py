def posLetra(s, l, n):
    """Recebe uma string, uma letra e um valor que indica a ocorrência da letra, retornando
    a posição dela na string. Falha, só funciona na primeira ocorrência
    """
    o = 0
    for i in list.s:
        if s[i] == l:
            o += 1
        if o == n:
            return i
    return -1