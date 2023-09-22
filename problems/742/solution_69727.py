# string, int, int -> string
def substitui(s,x,i):
    '''
    função retorna uma string igual a s, substituindo o 
    elemento da posição i pelo caractere x
    '''
    0 <= i >= len (s)
    return str  (s[:i] + x + s[i+1:])