def substitui(s,x,i):
    '''Função que substitui um caractere da string s pelo
    caractere x na posição i que vai de 0 até o comprimento
    da string s
    str, str, int -> str'''
    
    i = 0<=i<=len(s)
    return s.replace(s[i],x)