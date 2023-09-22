def substitui(s,x,i):
    '''função que recebe uma string s, um caractere x e um número inteiro i entre 0 
    e o comprimento da string, e retorna uma string igual a s, exceto que o elemento
    da posição i deve ser substituído pelo caractere x 
    entrada->str,int,int
    saida->str'''
    s = s[0:i] + x[i] + s[i+1]
    return s