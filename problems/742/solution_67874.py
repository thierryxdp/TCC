def substitui(s,x,i):
    '''
Funcao que substitui s, x e um inteiro(i) entre 0 e o
comprimento da string, exceto que o elemento da posicao i
seja substituido por x. Retorne s[0:i]+ x +s[i+1:]
string, int, int -> string
    '''
    return str(s[:i])+ str(x) +str(s[i+1:])