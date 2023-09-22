'''Função que recebe:
uma string (s);
um caractere (x);
um número int (i);
e retorna uma string igual a s, substituindo o int pelo caractere x 
string, int, int -> string'''
def substitui(s,x,i):
    return s[:i] + x + s [i + 1:]