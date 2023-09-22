def substitui(s,x,i):
    '''Função que, dados uma string s, um caractere x e um número inteiro i (sendo 0<=i<=len(str(s))), retorna uma string igual a s, exceto que o elemento da posição i deve ser substituído pelo caractere x.
str,int,int --> str'''
    return str(s)[0:i] + str(x) + str(s)[i+1:]