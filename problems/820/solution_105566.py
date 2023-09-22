def posLetra(fr, l, num):
    """
    assinatura:
    tuple(str, str, int) -> int
    testes:
    posLetra('abacate', 'a', 3) == 4 
    posLetra('ovo', 'o', 2) == 2 
    """
    if str.count(fr, l) < num:
        return -1
    else:
        return string.index(l)