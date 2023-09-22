def substitui(s,x,i):
    '''retorna uma str igual a str de entrada, porem o elemento da posicao i
    e substituido pelo caractere x
    str,str,int -> str'''
    return s[0:i]+str(x)+s[i+1:]