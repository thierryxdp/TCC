#Substitui posição i pelo caractere x
# string, int, int -> string
def substitui(s,x,i):
    x = bytearray(s) 
    x[i]= x
    s = str(x)
    print (s)