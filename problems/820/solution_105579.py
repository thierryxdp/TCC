def posLetra(f, l, x):
    """Com uma string, uma letra e um número, informa a posição da 
    string(f) em que a letra(l) está ocorrendo em x vezes
    str, str, int -> int"""
    y = 0
    z = 0
    a = list(f)
    if list.count(a, l) < x:
        return -1
    else:
        while y < x:
            if f[z] == l:
                y = y + 1
            else:
                None
            z = z + 1
        return z - 1