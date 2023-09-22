def substitui(s, x, i):
    """ Obtem uma string s e substitui o caractere na posição i pelo caractere x 
    str, str, int -> str """
    return s[:i]+x+s[i+1:]