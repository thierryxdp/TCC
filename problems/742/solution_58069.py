def substitui(s,x,i):
    '''funç˜ao definida que recebe uma string s, um caractere x e um
    número inteiro i entre 0 e o comprimento da string, e retorne uma string
    igual a s, exceto que o elemento da posiç˜ao i deve ser substituído pelo caractere x.
    string,int,int-> string'''
    return s[:i]+str(x)+s[i+1:]