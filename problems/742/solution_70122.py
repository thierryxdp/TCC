def substitui(s,x,i):
    "Substitui a posição da entrada i por x"
    "string, int, int -> string"
    return s[ :i]+x+s[(i+1): ]