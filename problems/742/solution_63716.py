def substitui(s,x,i):
    '''Recebe uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da str e substitui o caractere da posição i por x; str, str, int -> str'''
    return s[:i] + x + s[(i+1):]