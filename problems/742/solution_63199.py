def substitui(s,x,i):
    '''Recebe uma string s, um caractere x e um ńumero inteiro i entre 0 e o comprimento da string, e retorna uma string igual a s, exceto que o elemento da posiç̃ao i é substituído pelo caractere x
str, str, int -> str'''
    return s[:i]+'x'+s[i+1:]