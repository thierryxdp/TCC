'''Função que recebe:
uma string (s);
um caractere (x);
um número int (i);
e retorna uma string igual a s, substituindo o int pelo caractere x 
string, int, int -> string'''
def substitui(s,x,i):
    if i<0 or i>=(len(s)):
                      return "i inválido"
        else:
                      return s[:i] + x + s [i + 1:]