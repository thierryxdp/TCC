#substitui o caractere na posição i escolhida pelo caractere x
# entradas: string s, caractere x(str), i(numero inteiro)
#i seve estar entre zero e o comprimento da string s
# string, string, int -> string
def substitui(s,x,i):
    return s[:i]+x+s[(i+1):]