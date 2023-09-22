#Substitui posição i pelo caractere x
# string, int, int -> string
def substitui(s,x,i):
    x = s[i]
    a = s.replace('x',x)
    return str(a)