def substitui(s,x,i):
    '''funcao que recebe uma string s, um caractere x e um numero inteiro i entre 0 e o comprimento da string, e retorna uma string igual a s, exeto que o elemento da posisao i deve ser substituido pelo caractere x'''
    return s[:i]+x+s[i+1:]