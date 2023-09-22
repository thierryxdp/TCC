def substitui(s,x,i):
    '''
Funcao que substitui s, x e um inteiro(i) entre 0 e o
comprimento da string, exceto que o elemento da posicao i
seja substituido por x. 
(string, var, int -> string)
    '''
    return str(s[0:i]+ x +s[(i+1):])