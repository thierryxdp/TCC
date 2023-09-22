def substitui(s,x,i):
    '''função que recebe uma string s, 
    um caractere x
    e um número inteiro i
    e retorna uma string igual a s com i substituido pelo
    caractere x
    str str int -> str'''
    return s[:i]+x+s[i+1:]