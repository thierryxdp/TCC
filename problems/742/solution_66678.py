#Substitui posição i pelo caractere x
# string, int, int -> string
def substitui(s,x,i):
    y = s[i]
    l = list(s)
    l[i] = x
    a = "".join(l)
    return str(a)