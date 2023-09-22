def substitui(s,x,i):
    '''Função que retorna uma string igual a string incial s
    só que substitui o termo x na posição i; com 0<=i<len(s)
    valores: string, int, int -> string'''
    return s[0:i]+x+s[i+1:]