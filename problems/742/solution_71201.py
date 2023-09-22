# Substitui o caractere na posição i da string s pelo
# caractere x definido na função
# string, int, int -> string
def substitui(s,x,i):
    return x[:i-1]+x+[i+1:]