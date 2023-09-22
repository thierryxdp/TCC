# Calcula e retorna uma string igual a s, exceto que o elemento da posição i deve ser substituído pelo caractere x
# string, int, int -> string
def substitui(s,x,i):
    return s[0:i] + x + s[i+1:-1]