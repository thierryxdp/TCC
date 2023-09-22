def substitui(s,x,i):
    '''Retorne e calcule uma função que tem como entradas uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string igual a s, exceto que o elemento da posição i deve ser substítuido pelo caractere xx.
    string,int,int->string.'''
    s[i]=x
    return s
    return s[0:1]+x+s[i+1:]