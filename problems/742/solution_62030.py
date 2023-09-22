def substitui(s,x,i):
    """Funcao que recebe uma string s, um caractere x e um numero inteiro
i entre 0 e o comprimento da string, e retorna uma string igual a s, exceto
que o elemento da posicao i deve ser substituido pelo caractere x
; string, int, int -> string"""
    return s[0:i] + str(x) + s[i+1:]