def substitui(s,x,i):
    '''recebe uma string s um caracter x e um numero inteiro i entre 0 e o comprimento da string e retorna ua string igual a s exceto que o elemento da posiçao i deve ser substituido pelo caractere x''''
    '''str, str, int -> string'''
    return s[:i] + 'x' + s[i+1:]