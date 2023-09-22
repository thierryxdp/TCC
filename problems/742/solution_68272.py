def substitui(s,x,i):
    """ A função substitui uma letra da string original e retorna a modificação;
    str, str -> int """
    sub = s[:i] + x + s[1+i:]
    return sub