def substitui(s,x,i):
    """funcao que insere x numa posicao da string"""
    """string, int, int -> string"""
    i <= len(s)
    return s[:i]+x+s[i+1:]