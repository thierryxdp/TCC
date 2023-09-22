# retorna string com a posição i substituida pelo caractere x
# string, int, int -> string
def substitui(s,x,i):
    return s[:i] + x + s[i+1:]