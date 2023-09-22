def substitui(s,x,i):
    '''Recebe uma string s, um caractere x e um número inteiro i entre 0 
    e o comprimento da string, e retorna uma string igual a s, exceto que
    o elemento da posição i deve ser substituido pelo caractere x'''
    return s[0:i] + x + s[i+1 :]