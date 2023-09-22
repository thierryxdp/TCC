''' função que recebe uma string s, um caractere x e um numero
inteuro i entre 0 e o comprimento da string, retornando uma
string igual a s, exceto que o elemento da posição i deve ser 
substituido pelo caractere x '''
'''string, int, int -> string'''
def substitui(s,x,i):
    str[i]= x
    return str[0:i] + x + str[i+1:]