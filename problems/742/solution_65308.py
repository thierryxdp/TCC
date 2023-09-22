'''funçao que, fornecidos uma string (s), um caractere (x) e um numero
inteiro (i), o qual deve ser entre 0 e o comprimento da string, retorna
uma string igual a original, porem com o elemento da posiçao equivalente 
ao numero (i) substituido pelo caractere (x)
string, int, int -> string'''
def substitui(s,x,i):
    return s[0:i] + x + s[i+1:]