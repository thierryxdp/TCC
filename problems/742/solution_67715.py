# A função substitui um caracter específico em uma determinada posição por outro caracter dito.
# string, string, int -> string
def substitui(s,x,i):
     return(s[0:i]+x+s[i+1:])   
substitui