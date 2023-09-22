def substitui(s,x,i):
    """Função que substitui um elemento de um string
    string, int, int -> string """
    return s[:i] + str(x) + s[i+1:]