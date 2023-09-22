def substitui(s,x,i):
    '''Dado uma funcao que receba uma string s, um caractere x e um número inteiro i 
    entre 0 e o comprimento da string s, retorna uma string igual a s, 
    com o elemento da posição i substituido pelo caractere x
    str, str, int -> str'''
    return s[0:i]+x+s[i+1:]