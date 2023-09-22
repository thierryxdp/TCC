"Substitui o termo na psição i da string s pelo caracter x, retornando uma nova string
"string, string, int -> string"
def substitui(s,x,i):
    return s[0:i:] + x + s[i+1::]