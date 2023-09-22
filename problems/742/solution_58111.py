# Recebe uma string, um caractere e um número inteiro, retorna a mesma string
# porém com o elemento da posição do núm inteiro substituído pelo caractere
# string, string, int -> string
def substitui(s,x,i):
    return s[:i] + x + s[i+1:]