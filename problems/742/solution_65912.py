def substitui(s,x,i):
    #substitui um elemento da frase por outro caractere
    #string, int, int -> string
    s=str(s)
    x=str(x)
    l=list(s)
    l[i]=x
    s= "".join(l)
    return s