def substitui(s,x,i):
    '''uma funç˜ao definida por substitui(s, x, i) que receba uma string s, um caractere x e um
número inteiro i entre 0 e o comprimento da string, e retorne uma string igual a s, exceto que o elemento
da posição i deve ser substituído pelo caractere x'''
    ''' str,int > str'''
    if i > len(s):
      return print('i inválido')
    else:
        return s[0:i] + str(x) + s[i + 1:]