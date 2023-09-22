# Função que substitui um caractere de uma string
# string, string, int -> string
def substitui(s,x,i):
    
    new_s = s[:i] + x + s[i+1:]
    return new_s