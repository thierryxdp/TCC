def substitui(s,x,i):
    '''dado uma string, um caractere e um valor inteiro 
    entre 0 e o comprimento da string, retorna uma nova string.
    Essa nova string é a mesma, porem no caractere de posicao (i),
    sera colocado um caractere dado (x).
    string, int, int -> string'''
    parte1 = s[0:i]
    parte2 = s[i+1::]
    return parte1 + x + parte2