# Dada a string s, o caractere x e um inteiro i, esta função altera o 
# caracter da posição i da string s por x.
# string, int, int -> string
def substitui(s,x,i):
    nova_string = s[0:i] + x + s[i+1:]
    return nova_string