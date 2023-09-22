#Função que substitui posicionamento i para item x 
# string, int, int -> string
def substitui(s,x,i):
      if i>=0 and i<=len(s):
        return s[:i]+x+s[i+1:]