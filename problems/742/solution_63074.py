def substitui(s,x,i):
    """ Retorna um string s com seu elemento na posição i substituido por um carctere x; str, str, int -> str"""
    if 0 <= i <= len(s):
        return str.replace(s,s[i], x, 1)