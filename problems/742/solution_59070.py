def substitui(s,x,i):
    """retorna a mesma string s, mas com o caractere x no lugar de S[i]
    str, int, int -> str"""
    pparte = s[:i]
    sparte = s[i+1:]
    return pparte + str(x) + sparte