def substitui(s,x,i):
    '''Função que dado uma string s,um caractere x e um número inteiro i,
    entre 0 e o comprimento da string,retorna uma string igual a s,exceto
    que o elemento da posição i deve ser substituido pelo caractere x.
    str,str,int->str'''
    return s[:i]+x+s[i+1:]