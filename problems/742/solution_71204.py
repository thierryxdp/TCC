# Substitui o caractere na posição i da string s pelo
# caractere x definido na função
# string, int, int -> string
def substitui(s,x,i):
    return (s[:(i-1)])+(x)+(s[(i+1):])