def substitui(s,x,i):
    '''Funcao que recebe duas strings e subistui um caracter pelo numero de entrada;
    str,str,int -> str'''
#s: string
#x: caracter que substituto
#i: numero inteiro entre 0 e o comprimento da string
    s = list(s)
    s[i] = x
    nova_string = ''.join(s)
    return nova_string