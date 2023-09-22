def substitui(s,x,i):
    """ função que recebe uma string s, um caractere x e um número i, esse
        último é um inteiro entre 0 e o comprimento da string s, e retorna 
        uma string igual a s, exceto que o elemento da posição i deve ser 
        substituido pelo caractere x 
        str,str, int -> str"""
    y=i+1
    z=len(s)
    parte1str=s[0:i]
    parte2str=s[y:z]
    return parte1str + str(x) + parte2str