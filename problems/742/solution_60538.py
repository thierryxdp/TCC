# função que tendo uma string, um caractere e um numero que determina uma 
# posição da string como entrada retorna a mesma string com o elemento 
# original da string substituido pelo caractere informado na entrada 
# string, int, int -> string
def substitui(s,x,i):
    return s[0:i-1]+x+s[i+1:]