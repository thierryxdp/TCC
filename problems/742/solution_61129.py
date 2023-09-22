def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string.
    Retorna uma string igual a s, substituindo o elemento da posição i pelo caractere x;
    str, int, int -> str'''
    s[i] = x
    return s[0:i]+str(x)+s[i+1:]