def substitui(s,x,i):
    """retorna uma string igual a s, em que o elemento da posição i é substituido pelo caractere c.
    string, int, int-> string"""
    return s[:i]+x+s[i+1:]