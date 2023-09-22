# Funcao que recebe uma string 's', um numero inteiro 'i' que e entre 0 e o comprimento da string
# s,x,i
# string, int, int -> string
def substitui(s,x,i):
    D = s[0:i] + str(x) + s[i+1:]
    return D