# 
# string, int, int -> string
def substitui(s,x,i):
    """funcao que substitui x na posicao i da string s """
    
      return s[0:i] + x+ s[(i+1):]