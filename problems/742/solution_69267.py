def substitui(s,x,i):
    """Recebe uma palavra s, um caractere x e um numero do tamanho do lengh da palavra e substitui pela letra x no numero inserido
    	string, int, int -> string"""
    return s[:(i-1)]+s[x]+s[(x+1):len(s)]