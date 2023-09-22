def substitui(s,x,i):
    """ função que recebe uma sitring S, um caractere x e um número i, esse 
        último é um inteiro entre 0 e o comprimento da string, e retorna uma 
        string igual a s, exceto que o elemento da posição i deve ser 
        substituido pelo caractere x """
    parte1str=s[0:i]
    parte2str=s[-1:i]
    return str(parte1str) + str(x) + str(parte2str)