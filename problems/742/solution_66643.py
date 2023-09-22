#Substitui posição i pelo caractere x
# string, int, int -> string
def substitui(s,x,i):
  l = list(s)
l[i]= str(x)
s = ''.join(l)
print(s)