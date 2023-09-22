def substitui(s, x, i):
    """ substitui o caractere de uma string por outra
     s: str -> str  Texto inicial
     x: str -> str Caractere que vai alterar o texto
     i: int -> int Posicao onde o caractere (x) vai substituir em (s)
    :return:"""
    return s[:i] + x + s[i+1:]