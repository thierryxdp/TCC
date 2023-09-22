def substitui(s,x,i):
    """ Recebe uma string "s", um caractere qualquer "x" e um número
inteiro que varia de 0 até o número de caracteres da string e
retorna a mesma string mas com o caractere da posição "i" trocado
por "x".
string, string, float -> string
"""
    return s[:i] + x + s[i+1:]