def substitui(s,x,i):
    """Função que substitui um caracter da posição
    i da string s, por um dígito x, dados na entrada."""
    return s[0:i] + str(x) + s[i+1:len(s)]