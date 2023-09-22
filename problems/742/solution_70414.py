"""dada a funca retornar a string iguals exceto que o elemento da posicao i deve ser substituido peo caractere x"""
# string, int, int -> string
def substitui(s,x,i):
    s = s [0:i:] + x + s[i+1::] 
    return s