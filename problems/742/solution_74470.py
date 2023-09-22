def substitui(s,x,i):
    """parametros de entrada: str, str, int; retorno: str"""
    s=str(s)
    return s[0:i]+str(x)+s[i+1:]