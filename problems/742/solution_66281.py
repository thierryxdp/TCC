def substitui(s,x,i):
    """Retorna a string s com o caractere x no lugar o elemento i.
       str, int, int-> str"""
    return s[0:i] + str(x) + s[-1:i+1]