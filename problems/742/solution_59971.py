def substitui(s,x,i):
    """Dada uma string e dois caracteres x e i, retorna a string s com uma substituição do caracter na posição i pelo x.
    string, int, int -> string"""
    
    
    return s[:i] + x + s[i+1:]