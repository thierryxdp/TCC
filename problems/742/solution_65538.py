# Substitui uma letra por outra (x) em um texto (s) em uma posição (i)
# string, int, int -> string
def substitui(s,x,i):
    return s[0:i] + x + s[i + 1:]