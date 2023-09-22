def substitui(s,x,i):
    ''' função que recebe uma string s, um caractere x e um número inteiro i 
entre 0 e o comprimento da string, e retorna uma string igual a s, exceto 
que o elemento da posição i deve ser substituido pelo caracter j.
string, int, int -> string'''
    palavra = str.split(s,' ')
    palavra[i] = x
    return str.join(' ',palavra)