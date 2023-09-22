def posLetra(fr, l, num):
    """
    assinatura:
    tuple(str, str, int) -> int
    testes:
    posLetra('abacate', 'a', 3) == 4 
    posLetra('ovo', 'o', 2) == 2 
    """
    return str.find(fr, l, num)