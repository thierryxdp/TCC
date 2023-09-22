def substitui(str1,x,i):
    '''
Funcao que substitui s, x e um inteiro(i) entre 0 e o
comprimento da string, exceto que o elemento da posicao i
seja substituido por x. Retorne str1[0:i]+ x +str1[i+1:]
string, int, int -> string
    '''
    str1[i] = [0:i]+ x +str1[i+1:]
    return str1