def substitui(s,x,i):
    """Retorna uma nova string substituindo na str 's' o caracter 'x' na posicao í
    str, str, int -> str"""
    nova_str = s[:i] + x + s[(i+1):]
    return nova_str