"Substitui um caracter em um numero i de uma string" 
"s,x,i"
"string, string, int -> string
def substitui(s,x,i):
    return s[0:i] + x + s[i+1:]