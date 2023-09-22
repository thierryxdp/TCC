#  receba uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string, e retorne uma string igual a s, exceto que o elemento da posição i deve ser substituído pelo caractere x.
# s,x,i. Sendo s um string, x um caractere e i um numero inteiro.
# string, int, int -> string
def substitui(s,x,i):
    return s[0:i]+x+s[(i+1):]