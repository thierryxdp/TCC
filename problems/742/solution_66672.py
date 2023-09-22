#Substitui posição i pelo caractere x
# string, int, int -> string
def substitui(s,x,i):
    y = s[i]
    a = s.replace(y,x)
    return str(a)