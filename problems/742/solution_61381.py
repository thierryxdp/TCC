def substitui(s,x,i):
    """Substitui um caractere de uma palavra(s) na posição(i) pelo caractere(x)
    str, str, int --> str"""
    a = s[0:i]
    b = s[i:(len(s))]
         
    return str(a) + str(x) + str(b)