def substitui(s,x,i):
    """ Retorna um string s com seu elemento na posição i substituido por um carctere x; str, str, int -> str"""
    a = len(s)
    return (s[0:(i)]) + str(x) + str(s[(i+1):a])