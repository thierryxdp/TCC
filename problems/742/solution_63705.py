def substitui(s,x,i):
    """retorna uma string, igual a original, exceto que o elemento da posicao i, o qual deve ser um numero inteiro entre zero e o comprimento da string, sera substituido pelo caractere x;
    string, int, int ->string"""
    if i==0:
        return str(x)+s[1:]
    elif i>=1 and i<len(s):
        return s[0:]+str(x)+s[i+1:]
    else:
        return s[0:]-str(s[-1])+str(x)