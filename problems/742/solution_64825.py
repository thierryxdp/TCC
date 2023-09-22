def substitui(s,x,i):
    '''Funcao que recebe uma string s, um caractere x e um inteiro i que varia entre 0 e o comprimento da string e retorna uma string igual a s, entretanto com o elemento da posição i substituido por x; str, str, int -> str'''
    return s[0:i]+x+s[(i+1):]