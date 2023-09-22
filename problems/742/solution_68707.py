def substitui(s,x,i):
    """A função substitui um caractere 'i' por outro 'x'
    str-str-int--> str"""
    
    antes = s[0:i]
    depois = s[i+1:]
    resultado = antes + x + depois
    return resultado