def substitui(s,x,i):
    """retorna uma string, igual a original, exceto que o elemento da posicao i, o qual deve ser um numero inteiro entre zero e o comprimento da string, sera substituido pelo caractere x;
    string, int, int ->string"""
    return s[0:i]+str(x)+s[i+1:]