def substitui(s,x,i):
    '''Recebe uma string s, um caractere x e um numero inteiro i(entre 0 e o comprimento da string)
    e retorna uma string igual s porem com o elemento da posiçao i sendo x;
    string, int, int -> string'''
    return s[0:i]+x+s[i+1:]