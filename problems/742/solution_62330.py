def substitui(s,x,i):
    """Dado uma string s, retorna uma nova string que substitui o elemento de posição i da string pelo caracter x,"""
    """string, string, int -> string"""
    return s[0:i]+ str('x')+ s[i+1:]