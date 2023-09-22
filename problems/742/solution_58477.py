def substitui(s,x,i):
    '''Função que recebe como entrada uma string,um caractere e um número inteiro(s,x,i) e retorna uma string igual a s,exceto que o elemento da posição i deve ser substituido pelo caracterex.
    str,str,int->str'''
    s[i]=x
    return s[0:i]+x+s[i+1:]