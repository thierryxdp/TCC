def substitui(s,x,i):
    '''Recebe uma string(s) um caractere(x) e um numero(i) entre 0 e o comprimento da string
    e retorna uma string igual a s com o elemento da posição i substituido por x.
    string,int,int ->string'''
    return s[0:i]+str(x)+ s[i+1:]