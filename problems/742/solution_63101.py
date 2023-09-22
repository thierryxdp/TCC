def substitui(s,x,i):
    """Função que retorna uma string onde x é substituído por i.
    str, str, int --> str"""
    
    a = s[0:(i)]
    b = s[(i+1):(len(s))]
    return (str(a) + str(x) + str(b))