# A função recebe uma string s, um caractere x e um inteiro i( 0:comprimento da string) e retorna uma string igual a s
# s: string; x:int; i:int
# string, int, int -> string
def substitui(s,x,i):
    return s[0:i] + 'x' + s[i:]