def substitui(s,x,i):
    '''Essa função recebe uma string s, um caractere x e um número i, e retorno uma string igual a s, mas o elemento i sendo substituido pelo caractere x.
    str,str,int->str'''
    fim1=i
    return s[0:fim1]+x+s[fim1+1:len(s)]