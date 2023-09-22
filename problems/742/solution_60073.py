def substitui(s, x, i):
    """Funcao desenvolvida para substituir um caractere de uma string com outra string
    :param s: str -> str  Texto inicial
    :param x: str -> str Caractere que alterara o texto
    :param i: int -> int Posição onde o caractere (x) substituirá em (s)
    :return:"""
    return s[:i] + x + s[i+1:]