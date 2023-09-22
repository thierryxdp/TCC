def substitui(s, x, i):
    '''recebe string (s), um caractere (x) e um numero (i), tal que 0 < i < total de caracteres de s.
    Substitui o caractere de poisicao i da string s por x.
    str, str, int --> str'''
    novo_s = list(s)
    novo_s[i] = x
    s_junto = "".join(novo_s)
    return s_junto