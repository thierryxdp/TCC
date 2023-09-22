# Fuçao que recebe string, um caractere e um numero inteiro entre 0 e o
# comprimento da string e retorna uma string igual, porem o elemento da 
# posição é trocado pelo caractere  
# string, int, int -> string
def substitui(s,x,i):
    s[i] = x
    if i == 0:
        return str(x)+s[i:]
    else: 
    return s[:i] + str(x) + s[i + 1:]