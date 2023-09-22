def substitui(s,x,i):
    """Substitui <i> que será um número inteiro que localiza
o caracter na string por "x".
#<i> tem que estar entre 0 e o comprimento da string.
assinatura: string, int, int -> string
casos de testes:
substitui('isabella', '6', 2) == 'is6bella'
substitui('daniel', 'p', 0) == 'paniel'
substitui('galo', 't', 2) == 'gato'
substitui('bala', 's', 0) == 'sala'
"""
    return s[:i] + x + s[i+1:]