def substitui(s, x, i):
    '''recebe string (s), um caractere (x) e um numero (i), tal que 0 < i < total de caracteres de s.
    Substitui o caractere de poisicao i da string s por x.
    str, str, int --> str'''
    return s.replace(s[i], x)