def substitui(s,x,i):
    """Calcula e retorna a uma string, dado o caracter "x", uma string "s" e um
numero inteiro "i", entre zero e o comprimento da str; str, caracter, int -->
str"""
    p=i-1
    y= s[:(p)]+"x"+s[i:]
    return y