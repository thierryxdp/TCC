def substitui(s,x,i):
    """Função recebe uma str (s), um caractere (x) e um int (i)
    entre 0 e o comprimento da str, e depois retorna ums string
    igual a s com certas exceções; str, int, int -> str"""
    return s[0:i] + x + s[i + 1:]