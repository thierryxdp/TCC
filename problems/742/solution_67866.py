def substitui(str1, x, i):
    '''
Funcao que substitui s, x e um inteiro(i) entre 0 e o
comprimento da string, exceto que o elemento da posicao i
seja substituido por x. Retorne str1[0:i]+ x +str1[i+1:]
int -> string
    '''
    str1[i] = x
    return str1[0:i]+ x +str1[i+1:]