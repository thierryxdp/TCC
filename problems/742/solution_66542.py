# Recebe uma string s, um caracter x e um numero inteiro i entre 0 e o comprimento da string, e retorna uma string igual a s, exceto que o elemento da posição i é substituido por 
# string, int, int -> string
def substitui(s,x,i):
    return s[0:i] + x + s[i + 1:]