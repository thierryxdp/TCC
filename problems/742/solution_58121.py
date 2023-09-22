def substitui(s,x,i):
    """ recebe uma string s, um caractere x e um numero inteiro i entre 0 e o comprimento da string e retorna uma string igual a s, exceto que o elemento da posicao i deve ser substituido pelo x""""
    return s[0:'i']+['x']+s['i':len(s)]