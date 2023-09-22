def posLetra(frase, l, x):
    """Dada uma string, uma letra e um número, indica a posição da string em que a letra está considerando a ocorrência número x(número)
    str, str, int -> int"""
    y = 0
    z = 0
    a = list(frase)
    if list.count(a, l) < x:
        return -1
    else:
        while y < x:
            if frase[z] == l:
                y = y + 1
            else:
                None
            z = z + 1
        return z - 1