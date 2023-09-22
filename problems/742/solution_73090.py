def substitui(s,x,i):
    """ o caractere 'x' será substituido na string (s), na posição do numero inteiro (i). 
    Portanto i deve estar entre 0 e o comprimento da string, ou ser igual a zero"""
    if (0 <= i <= len(s)):
            return ( s[:i] + x + s[i+1:])
    else:
        return str ("i deve ser um numero inteiro entre 0 e comprimento da string")