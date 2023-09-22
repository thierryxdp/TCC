def substitui(s,x,i):
    '''
    Funcao que substitui um caractere da string original por um outro caractere x,
    com base na posição definida por um numero inteiro (i)
    
    s = String original
    x = caractere novo que entra no lugar de um caractere do string original
    i = numero inteiro que esta no intervalo 0<i<len(s)
    str, int, int -> str
    '''
    if i == 0:
        return x+s[1:]
    elif i == [len(s)]:
        return s[len(s)] + x
    elif i == i>0 :
        return s[0:i] + x + s[i+1:]